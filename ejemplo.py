#!/usr/bin/python
# -*- coding: utf-8 -*-

def pares(number1,number2):
    if number2 < number1:
        print(f"¡Le he pedido un número entero mayor o igual que {numero_1}!")
        print("False")
        return False
    else:
        for i in range(number1, number2 + 1):
            if i % 2 == 0:
                print(f"El número {i} es par.")
                print("True")
    return True

pares(1000,3000)
