#!/usr/bin/python3
""" 101-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    list_rectangles = [Rectangle(100, 10, 200, 200), Rectangle(90, 110, 50, 110), Rectangle(50, 20, 100, 100)]
    list_squares = [Square(50, 200, 500), Square(90, 300, 50), Square(80, 200, 400)]

    Base.draw(list_rectangles, list_squares)
