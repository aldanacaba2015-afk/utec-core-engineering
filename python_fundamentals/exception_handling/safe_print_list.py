#!/usr/bin/env python3
"""Funcion que imprime x elementos de una lista de forma segura."""


def safe_print_list(my_list=[], x=0):
    """Imprime hasta x elementos y devuelve la cantidad real impresa."""
    printed = 0
    try:
        while printed < x:
            print(my_list[printed], end="")
            printed += 1
    except IndexError:
        pass
    print()
    return printed
