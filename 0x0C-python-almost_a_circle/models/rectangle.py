#!/usr/bin/python3
"""
The class rectangle will inherit
"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle template with the use of Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialized the rectangle with desired global id """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        # Getter and setter for width
    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value
    # ----------- -----------------

    # Getter and setter for height
    @property
    def height(self):
        """ width getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value
    # ----------- -----------------

    # Getter and setter for x
    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value
    # ----------- -----------------

    # Getter and setter for x
    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value
    # ----------- ----------------- ----

    def area(self):
        """ method to define the area of a rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """ method to display a rectangle """
        for lines in range(self.__y):
            print("")
        for row in range(self.__height):
            for spaces in range(self.__x):
                print(" ", end="")
            for col in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """prints the rectangle information """
        return("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ Update class variables """
        if kwargs and args is None or args is ():
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            if i == 1:
                self.width = args[i]
            if i == 2:
                self.height = args[i]
            if i == 3:
                self.x = args[i]
            if i == 4:
                self.y = args[i]

    def to_dictionary(self):
        """sends instance rep in dict format"""
        new_dict = {}
        for key, value in self.__dict__.items():
            new_dict[key.split("_")[-1]] = value
        return(new_dict)
