#!/usr/bin/env python3
"""Calcula la potencia de un numero usando un bucle."""


def pow(a, b):
    """Devuelve a elevado a la potencia b usando multiplicacion repetida."""
    result = 1
    for _ in range(abs(b)):
        result *= a
    if b < 0:
        return 1 / result
    return result


def main():
    """Ejecuta casos de demostracion."""
    print(pow(2, 4))
    print(pow(5, 0))


if __name__ == "__main__":
    main()
