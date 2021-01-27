#!/usr/bin/python3
"""in this module is the base function"""

from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """this initialize the variables"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter width"""
        return self.__width

    @width.setter
    def width(self, v_width):
        """setter width"""
        if type(v_width) is not int:
            raise TypeError("width must be an integer")
        elif v_width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = v_width

    @property
    def height(self):
        """getter height"""
        return self.__height

    @height.setter
    def height(self, v_height):
        """setter height"""
        if type(v_height) is not int:
            raise TypeError("height must be an integer")
        elif v_height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = v_height

    @property
    def x(self):
        """getter x"""
        return self.__x

    @x.setter
    def x(self, v_x):
        """setter x"""
        if type(v_x) is not int:
            raise TypeError("x must be an integer")
        elif v_x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = v_x

    @property
    def y(self):
        """getter y"""
        return self.__y

    @y.setter
    def y(self, v_y):
        """setter y"""
        if type(v_y) is not int:
            raise TypeError("y must be an integer")
        elif v_y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = v_y

    def area(self):
        """getter area"""
        return (self.width * self.height)

    def display(self):
        """shows a representation of rectangle with #"""
        print('\n' * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        '''override the __str__ method so that it returns'''
        ret = "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return ret.format(self.__class__.__name__,
                          self.id, self.x, self.y, self.width, self.height)

    def update(self, *args,  **kwargs):
        '''Update the class Rectangle'''
        AttList = ["id", "width", "height", "x", "y"]
        size_list = len(AttList)
        cont = 0
        if args and len(args) != 0:
            for arg in args:
                if cont == 0:
                    super().__init__(arg)
                elif cont < size_list:
                    setattr(self, AttList[cont], arg)
                cont += 1
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == "id":
                        super().__init__(value)
                    else:
                        setattr(self, key, value)

    def to_dictionary(self):
        '''returns a dictionary with the variables'''
        dic = {'id': self.id, 'width': self.width,
               'height': self.height, 'x': self.x, 'y': self.y}
        return dic
