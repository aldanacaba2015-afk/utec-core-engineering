#!/usr/bin/env python3
"""Funcion que divide dos enteros de forma segura."""


def safe_print_division(a, b):
    """Divide a entre b y maneja excepciones."""
    result = None
    try:
        result = a / b
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
