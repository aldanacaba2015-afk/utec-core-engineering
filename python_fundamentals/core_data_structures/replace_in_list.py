#!/usr/bin/env python3
"""Funcion que reemplaza un elemento de una lista en una posicion especifica."""


def replace_in_list(my_list, idx, element):
    """Reemplaza el elemento en la posicion idx o devuelve la lista original."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
