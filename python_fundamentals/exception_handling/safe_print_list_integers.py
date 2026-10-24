#!/usr/bin/env python3
"""Funcion que imprime enteros de una lista de forma segura."""


def safe_print_list_integers(my_list=[], x=0):
    """Imprime solo enteros y devuelve la cantidad real impresa."""
    printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (TypeError, ValueError):
            continue
        printed += 1
    print()
    return printed
