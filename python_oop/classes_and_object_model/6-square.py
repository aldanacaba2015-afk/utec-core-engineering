#!/usr/bin/env python3
"""Modulo que define la clase Square."""


class Square:
    """Representa un cuadrado con tamano y posicion privados."""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa el cuadrado usando los setters para validar."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Devuelve el tamano del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece el tamano con validacion de tipo y valor."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Devuelve la posicion del cuadrado."""
        return self.__position

    @position.setter
    def position(self, value):
        """Establece la posicion validando tupla de dos enteros."""
        message = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple or len(value) != 2:
            raise TypeError(message)
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError(message)
        if value[0] < 0 or value[1] < 0:
            raise TypeError(message)
        self.__position = value

    def area(self):
        """Devuelve el area del cuadrado."""
        return self.__size * self.__size

    def my_print(self):
        """Imprime el cuadrado con el caracter #."""
        print(self.__str__())

    def __str__(self):
        """Devuelve la representacion en cadena del cuadrado."""
        if self.__size == 0:
            return ""
        lines = [""] * self.__position[1]
        row = " " * self.__position[0] + "#" * self.__size
        lines.extend([row] * self.__size)
        return "\n".join(lines)
