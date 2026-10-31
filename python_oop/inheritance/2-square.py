#!/usr/bin/env python3
"""Modulo que define la clase Square."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Representa un cuadrado (rectangulo con ancho y alto iguales)."""

    def __init__(self, size):
        """Inicializa el cuadrado con un tamano validado."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Devuelve la representacion en cadena del cuadrado."""
        return "[Square] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height)
