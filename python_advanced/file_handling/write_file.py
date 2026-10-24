#!/usr/bin/env python3
"""Funcion que escribe una cadena en un archivo de texto UTF-8."""


def write_file(filename="", text=""):
    """Escribe text en filename y devuelve el numero de caracteres escritos."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
