#!/usr/bin/python3
"""
This class will be the “base” of all other classes in this project.
The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)
"""
import json
import os
import csv
import turtle
import random


class Base():
    """Base object template"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Base init for object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the json rep of a list of dictionaries

        Args:
            list_dictionaries ([list]): dict lis

        Returns:
            json: dict in json format
        """
        if list_dictionaries:
            return (json.dumps(list_dictionaries))
        return("[]")

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves class and list of objects into a file

        Args:
            list_objs (int): list with the instances
        """
        if list_objs is not None:
            dict_list = [x.to_dictionary() for x in list_objs]
        else:
            dict_list = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as my_file:
            my_file.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of json string

        Args:
            json_string ([list]): [list of dictionaries]

        Returns:
            list represented by json string
        """
        if json_string:
            return(json.loads(json_string))
        return ([])

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance from a dictionary
        """
        if (cls.__name__ == "Square"):
            dummy = cls(2)
        elif (cls.__name__ == "Rectangle"):
            dummy = cls(2, 2)
        dummy.update(**dictionary)
        return(dummy)

    @classmethod
    def load_from_file(cls):
        """Loads file and returns a list of instances
        """
        instance_list = []
        filename = cls.__name__ + ".json"
        if not os.path.isfile(filename):
            return (instance_list)
        with open(filename) as my_file:
            my_data = cls.from_json_string(my_file.read())
            for instance in my_data:
                instance_list.append(cls.create(**instance))
        return (instance_list)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves instance dict inf, in a csv file

        Args:
            list_objs (list): [List of csv files]
        """
        dict_list = [x.to_dictionary() for x in list_objs]
        filename = cls.__name__ + ".csv"
        if (cls.__name__ == "Rectangle"):
            header_list = ["id", "width", "height", "x", "y"]
        elif (cls.__name__ == "Square"):
            header_list = ["id", "size", "x", "y"]
        with open(filename, "w") as my_file:
            writer = csv.DictWriter(my_file, fieldnames=header_list)
            writer.writeheader()
            for my_dict in list_objs:
                writer.writerow(my_dict.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Loads csv and return list of instances with those
            characteristics
        """
        instance_list = []
        filename = cls.__name__ + ".csv"
        if not os.path.isfile(filename):
            return (instance_list)
        with open(filename) as my_file:
            csv_reader = csv.DictReader(my_file)
            for row in csv_reader:
                row = {key: int(row[key]) for key in row.keys()}
                instance_list.append(cls.create(**row))
        return(instance_list)

    @staticmethod
    def draw_rectangle(board, x, y, width, height, fill):
        """Draws a rectangle with a pencil animation

        Args:
            board (turtle board): Turtle board to draw on
            x ([int]): x position
            y ([int]): y position
            width ([int]): rec width
            height ([int]): rec height
            color ([list]): color to draw the line
            fill ([str]): fill color
        """
        board.fillcolor(fill)
        font = ("Arial", 8, 'normal', 'bold', 'italic', 'underline')
        color = [random.random() for x in range(3)]
        board.speed(1)
        board.pencolor(color[0], color[1], color[2])
        board.pensize(3)
        board.setheading(0)
        board.begin_fill()
        board.up()
        board.goto(x, y)
        board.down()
        # draw top
        board.forward(width)
        # draw right
        board.right(90)
        board.write("   Height = "+str(height)+" px", font=font)
        board.forward(height)
        # draw bottom
        board.right(90)
        board.forward(width)
        # draw left
        board.right(90)
        board.forward(height)
        board.end_fill()
        board.up()
        board.goto(x, y + 20)
        board.down()
        board.write("Width = "+str(width)+" px", font=font)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws the rectangle and squares.

        Args:
            list_rectangles (list): List with instances with rectangle
            list_squares (list): List with instances of squares
        """

        font = ("Arial", 15, 'normal', 'bold')
        dict_list = [x.to_dictionary() for x in list_rectangles]
        square_list = [y.to_dictionary() for y in list_squares]
        wn = turtle.Screen()
        wn.title("Display your figures")
        board = turtle.Turtle()
        wn_size = (600, 600)
        wn.setup(width=wn_size[0], height=wn_size[1], startx=0, starty=0)
        wn.setworldcoordinates(0, wn_size[0], wn_size[1], -50)
        # len (first object)
        for my_dict in dict_list:
            Base.draw_rectangle(board, my_dict["x"], my_dict["y"],
                                my_dict["width"], my_dict["height"], "red")
        for my_dict in square_list:
            Base.draw_rectangle(board, my_dict["x"], my_dict["y"],
                                my_dict["size"], my_dict["size"], "blue")
        board.up()
        board.goto(wn_size[0] / 2, wn_size[1] / 2)
        board.write("Sq_lis len = "+str(len(square_list)), font=font)
        board.goto(wn_size[0] / 2, (wn_size[1] / 2) + 20)
        board.write("Rec_lis len = " + str(len(dict_list)), font=font)
        board.down()
        input()
