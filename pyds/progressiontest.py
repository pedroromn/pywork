# -*- coding:utf-8 -*-


from progression import *


def main():
    print("Default progression: ")
    Progression().print_progression(10)

    print("Arithmetic progression with increment 5: ")
    ArithmeticProgression(5).print_progression(10)

    print("Arithmetic progression with increment 5 and start 2: ")
    ArithmeticProgression(5, 2).print_progression(10)

    print("Geometric progression with default base: ")
    GeometricProgression().print_progression(10)

    print("Geometric progression with base 3: ")
    GeometricProgression(3).print_progression(10)

    print("Fibonacci progression with default start values: ")
    FibonacciProgression().print_progression(10)

    print("Fibonacci progression with start value 4 and 6: ")
    FibonacciProgression(4, 6).print_progression(10)

if __name__ == '__main__':
    main()
