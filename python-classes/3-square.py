#!/usr/bin/python3
"""
Bu modul kvadratın ölçüsünü yoxlayan və sahəsini
hesablayan Square klasını təyin edir.
"""


class Square:
    """
    Kvadratı təmsil edən klas.
    """

    def __init__(self, size=0):
        """
        Yeni bir Square nümunəsini yaradır.

        Args:
            size (int): Kvadratın tərəfinin ölçüsü. Default 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Kvadratın cari sahəsini hesablayır.

        Returns:
            Kvadratın sahəsi (size * size).
        """
        return self.__size ** 2
