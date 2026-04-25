#!/usr/bin/python3
"""
Bu modul kvadratın ölçüsünü yoxlayan (validation)
Square klasını təyin edir.
"""


class Square:
    """
    Kvadratı təmsil edən klas.
    """

    def __init__(self, size=0):
        """
        Yeni bir Square nümunəsini yaradır və daxil edilən
        ölçünü yoxlayır.

        Args:
            size (int): Kvadratın tərəfinin ölçüsü. Default 0.

        Raises:
            TypeError: Əgər size integer deyilsə.
            ValueError: Əgər size 0-dan kiçikdirsə.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
