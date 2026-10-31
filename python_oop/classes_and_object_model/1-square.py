#!/usr/bin/env python3
"""Modulo que define la clase Square."""


class Square:
    """Representa un cuadrado con un tamano privado."""

    def __init__(self, size):
        """Inicializa el cuadrado con un tamano dado."""
        self.__size = size
