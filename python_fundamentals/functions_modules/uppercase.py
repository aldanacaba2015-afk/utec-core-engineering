#!/usr/bin/env python3
"""Convierte una cadena a mayúsculas usando lógica ASCII."""


def uppercase(str):
    """Imprime la cadena en mayúsculas usando ASCII sin usar .upper()."""
    for c in str:
        code = ord(c)
        if 97 <= code <= 122:
            print("{}".format(chr(code - 32)), end="")
        else:
            print("{}".format(c), end="")
    print()


def main():
    """Ejecuta casos de demostración."""
    uppercase("Holberton")
    uppercase("hello world")
    uppercase("Python 3.8")


if __name__ == "__main__":
    main()
