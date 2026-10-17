#!/usr/bin/env python3
"""Imprime y devuelve el último dígito de un número."""


def print_last_digit(number):
    """Imprime el último dígito de number y lo devuelve como positivo."""
    last_digit = abs(number) % 10
    print(last_digit)
    return last_digit


def main():
    """Ejecuta casos de demostración."""
    print_last_digit(98)
    print_last_digit(-1024)
    print_last_digit(0)
    print_last_digit(-7)


if __name__ == "__main__":
    main()
    # Última actualización: corrección de errs
