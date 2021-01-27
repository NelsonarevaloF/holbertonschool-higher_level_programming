#!/usr/bin/python3
"""in this module is the base Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """this initialize the variables"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        '''override the __str__ method so that it returns'''
        ret = "[{:s}] ({:d}) {:d}/{:d} - {:d}"
        return ret.format(self.__class__.__name__,
                          self.id, self.x, self.y, self.width)

    def update(self, *args,  **kwargs):
        '''Update the class Square'''
        AttList = ["id", "size", "x", "y"]
        size_list = len(AttList)
        cont = 0
        if args and len(args) != 0:
            for arg in args:
                if cont == 0:
                    super().update(arg)
                elif cont < size_list:
                    setattr(self, AttList[cont], arg)
                cont += 1
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == "id":
                        super().update(value)
                    else:
                        setattr(self, key, value)

    def to_dictionary(self):
        '''returns a dictionary with the variables'''
        dic = {'id': self.id, 'size': self.size,
               'x': self.x, 'y': self.y}
        return dic
