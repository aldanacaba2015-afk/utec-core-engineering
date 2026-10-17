#!/usr/bin/env python3
"""Verifica si un carácter es una letra minúscula usando lógica ASCII."""


def islower(c):
    """Devuelve True si c es una letra minúscula, False en caso contrario."""
    code = ord(c)
    return 97 <= code <= 122


def main():
    """Ejecuta casos de demostración."""
    print(islower('a'))
    print(islower('A'))
    print(islower('3'))


if __name__ == "__main__":
    main()
