#!/usr/bin/env python3
"""Modulo que define la clase Square."""


class Square:
    """Representa un cuadrado con un tamano privado validado."""

    def __init__(self, size=0):
        """Inicializa el cuadrado con validacion de tipo y valor."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Devuelve el area del cuadrado."""
        return self.__size * self.__size
