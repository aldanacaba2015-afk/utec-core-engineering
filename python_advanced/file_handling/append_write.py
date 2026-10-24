#!/usr/bin/env python3
"""Funcion que anade una cadena al final de un archivo de texto UTF-8."""


def append_write(filename="", text=""):
    """Anade text al final de filename y devuelve los caracteres anadidos."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
