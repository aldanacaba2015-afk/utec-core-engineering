#!/usr/bin/env python3
"""Funcion que lee un archivo de texto y lo imprime en stdout."""


def read_file(filename=""):
    """Lee filename y lo imprime sin agregar saltos extra."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
