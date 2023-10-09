#!/usr/bin/python3
"""create a class square and calculate the area of the square then print it"""


class Square:
    """this is the class named square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize size and position"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """get the size"""
        return self.__size

    @property
    def position(self):
        """get the position"""
        return self.__position

    @size.setter
    def size(self, value):
        """set the value for size"""
        if value < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """set the value for position"""
        test = [isinstance(numb, int) and numb >= 0 for numb in value]
        if len(value) != 2 or not test:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """calculate the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """print the square with # """
        if self.__size == 0:
            print()
        else:
            for row in range(self.__size):
                if self.__position[1] <= 0:
                    for i in range(self.__position[0]):
                        print(" ", end="")
                for col in range(self.__size):
                    print("#", end="")
                print()
