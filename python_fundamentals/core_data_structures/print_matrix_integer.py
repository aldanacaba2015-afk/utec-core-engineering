#!/usr/bin/env python3
"""Funcion que imprime una matriz de enteros."""


def print_matrix_integer(matrix=[[]]):
    """Imprime cada fila de matrix en su propia linea."""
    for row in matrix:
        line = " ".join("{:d}".format(v) for v in row)
        print(line)
