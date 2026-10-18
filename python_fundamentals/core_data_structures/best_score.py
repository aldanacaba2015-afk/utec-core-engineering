#!/usr/bin/env python3
"""Funcion que devuelve la clave con el valor entero mas grande."""


def best_score(a_dictionary):
    """Devuelve la clave con el valor maximo o None si esta vacio."""
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
