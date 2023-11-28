#!/usr/bin/python3
"""create a class Base"""
import json


class Base:
    """this the class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize id in case of id is not none otherwise
        we increment nb_objects and assign its value to id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = "{}.json".format(cls.__name__)
        list = []
        for obj in list_objs:
            list.append(obj.to_dictionary())
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON
        string representation json_string:"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Square":
            dummy = cls(size=8)
        elif cls.__name__ == "Rectangle":
            dummy = cls(height=8, width=8)
        dummy.update(**dictionary)
        return dummy
    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename ="{}.json".format(cls.__name__)
        if filename is None:
            return []
        else:
            with open(filename, "r") as f:
                cont = f.read()
                list = cls.from_json_string(cont)
                instan_l = []
                for dict in list:
                    instan = cls.create(**dict)
                    instan_l.append(instan)
                return instan_l
class Rectangle(Base):
    """this is the class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize width,height,x,y and id
        super() is a builtin function that allow us to acces
        method of the Base class and then we can initialize
        id using __init__because id is a part of Base
        not Rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """retrieve value of width """
        return self.__width

    @width.setter
    def width(self, width):
        """set value to width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """retrieve value of height """
        return self.__height

    @height.setter
    def height(self, height):
        """set value to height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """retrieve value of x """
        return self.__x

    @x.setter
    def x(self, x):
        """set value to x"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """retrieve value of y """
        return self.__y

    @y.setter
    def y(self, y):
        """set value to y"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """calculate the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """display the rectangle"""
        if self.__y > 0:
            for i in range(self.__y):
                print()
        for i in range(self.__height):
            if self.__x > 0:
                for i in range(self.__x):
                    print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """[Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assign an argument to each attribute"""
        if len(args) != 0:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.__width = args[1]
            elif len(args) == 3:
                self.__height = args[2]
            elif len(args) == 4:
                self.__x = args[3]
            elif len(args) == 5:
                self.__y = args[4]
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.__width = v
                elif k == "height":
                    self.__height = v
                elif k == "x":
                    self.__x = v
                elif k == "y":
                    self.__y = v

    def to_dictionary(self):
        """return the dictionary representation of a Rectangle"""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width}
class Square(Rectangle):
    """this is the square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """use all attributes of Rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """[Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """retrieve  the value of size"""
        return self.width

    @size.setter
    def size(self, size):
        """assign size to width and height"""
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """assign argument to each attribute"""
        if len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            elif len(args) >= 2:
                self.size = args[1]
            elif len(args) >= 3:
                self.x = args[2]
            elif len(args) >= 4:
                self.y = args[3]
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """return the dictionary representation of a Square"""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}


r1 = Rectangle(10, 7, 2, 8)
r2 = Rectangle(2, 4)
list_rectangles_input = [r1, r2]

Rectangle.save_to_file(list_rectangles_input)

list_rectangles_output = Rectangle.load_from_file()

for rect in list_rectangles_input:
    print("[{}] {}".format(id(rect), rect))

print("---")

for rect in list_rectangles_output:
    print("[{}] {}".format(id(rect), rect))

print("---")
print("---")

s1 = Square(5)
s2 = Square(7, 9, 1)
list_squares_input = [s1, s2]

Square.save_to_file(list_squares_input)

list_squares_output = Square.load_from_file()

for square in list_squares_input:
    print("[{}] {}".format(id(square), square))

print("---")

for square in list_squares_output:
    print("[{}] {}".format(id(square), square))