#!/usr/bin/env python3
"""Demostracion de herencia y polimorfismo."""


class Animal:
    """Representa un animal generico."""

    def speak(self):
        """Devuelve el sonido del animal."""
        return "Some sound"


class Dog(Animal):
    """Representa un perro."""

    def speak(self):
        """Devuelve el ladrido del perro."""
        return "Woof"


class Cat(Animal):
    """Representa un gato."""

    def speak(self):
        """Devuelve el maullido del gato."""
        return "Meow"


if __name__ == "__main__":
    # Paso 3: Crear objetos
    dog = Dog()
    cat = Cat()

    print("Paso 3 - Objetos individuales:")
    print(dog.speak())
    print(cat.speak())

    print()

    # Paso 5: Demostrar polimorfismo
    print("Paso 5 - Polimorfismo con lista:")
    animals = [Dog(), Cat(), Dog()]

    for animal in animals:
        print(animal.speak())

    print()

    # Paso 6: Comprobar relaciones entre clases
    print("Paso 6 - Relaciones entre clases:")
    print(f"isinstance(dog, Dog): {isinstance(dog, Dog)}")
    print(f"isinstance(dog, Animal): {isinstance(dog, Animal)}")
    print(f"issubclass(Dog, Animal): {issubclass(Dog, Animal)}")
