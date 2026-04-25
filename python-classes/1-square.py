#!/usr/bin/python3
"""
Bu modul ölçüsü olan bir Square klasını təyin edir.
"""


class Square:
    """
    Kvadratı təmsil edən klas.
    """

    def __init__(self, size):
        """
        Yeni bir Square nümunəsini yaradır.

        Args:
            size: Kvadratın tərəfinin ölçüsü.
        """
        self.__size = size
