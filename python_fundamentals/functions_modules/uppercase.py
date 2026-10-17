#!/usr/bin/env python3
"""Convierte una cadena a mayúsculas usando lógica ASCII."""


def uppercase(str):
    """Imprime la cadena en mayúsculas seguida de una nueva línea.

    Usa códigos ASCII (ord y chr) para convertir cada carácter
    minúsculo a su equivalente en mayúscula, sin usar .upper().
    No devuelve ningún valor.
    """
    result = ""
    for c in str:
        code = ord(c)
        if 97 <= code <= 122:
            result += chr(code - 32)
        else:
            result += c
    print(result)


def main():
    """Ejecuta casos de demostración."""
    uppercase("Holberton")
    uppercase("hello world")
    uppercase("Python 3.8")
    uppercase("123 ABC xyz")


if __name__ == "__main__":
    main()
