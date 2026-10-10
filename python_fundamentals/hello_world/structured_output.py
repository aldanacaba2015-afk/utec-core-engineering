#!/usr/bin/env python3
"""
Módulo que imprime información estructurada sobre Python.
"""


def main():
    """Genera y muestra la salida determinista requerida."""
    # Variables según restricciones
    language = "Python"
    version = 3
    pi_val = 22 / 7
    is_valid = 10 > 5

    # Salida con interpolación y formato a dos decimales
    print(f"Language: {language}")
    print(f"Version: {version}")
    print(f"Pi approx: {pi_val:.2f}")
    print(f"Computation valid: {is_valid}")


if __name__ == "__main__":
    main()
