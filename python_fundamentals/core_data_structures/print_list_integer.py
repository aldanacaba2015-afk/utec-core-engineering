#!/usr/bin/env python3
"""Funcion que imprime todos los enteros de una lista."""


def print_list_integer(my_list=[]):
    """Imprime cada entero de my_list en su propia linea."""
    for i in my_list:
        print("{:d}".format(i))
