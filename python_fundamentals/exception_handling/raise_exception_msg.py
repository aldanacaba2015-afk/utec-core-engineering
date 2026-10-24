#!/usr/bin/env python3
"""Funcion que lanza un NameError con un mensaje personalizado."""


def raise_exception_msg(message=""):
    """Lanza un NameError con el mensaje proporcionado."""
    raise NameError(message)
