#!/usr/bin/env python3
"""Imprime y devuelve el ultimo digito de un numero."""


def print_last_digit(number):
    """Imprime el ultimo digito de number y lo devuelve como positivo."""
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit


def main():
    """Ejecuta casos de demostracion."""
    print_last_digit(98)
    print()
    print_last_digit(-1024)
    print()


if __name__ == "__main__":
    main()
