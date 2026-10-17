#!/usr/bin/env python3
"""Programa que importa add() y calcula 1 + 2."""

from add_0 import add

if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
