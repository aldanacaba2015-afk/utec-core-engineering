#!/usr/bin/env python3
"""Modulo que define la clase Rectangle."""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectangulo definido por ancho y alto."""

    def __init__(self, width, height):
        """Inicializa el rectangulo con ancho y alto validados."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
