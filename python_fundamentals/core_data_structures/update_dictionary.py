#!/usr/bin/env python3
"""Funcion que reemplaza o agrega un par clave/valor."""


def update_dictionary(a_dictionary, key, value):
    """Reemplaza o agrega key con value y devuelve el diccionario."""
    a_dictionary[key] = value
    return a_dictionary
