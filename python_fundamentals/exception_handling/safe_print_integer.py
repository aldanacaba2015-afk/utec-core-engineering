#!/usr/bin/env python3
"""Funcion que imprime un entero de forma segura."""


def safe_print_integer(value):
    """Imprime value si es entero y devuelve True, o False en otro caso."""
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
