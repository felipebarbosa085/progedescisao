"""Desenvolver um programa que pergunte um número e exiba a informação de que ele é positivo, negativo ou
nulo"""

num1 = int(input("Qual o numero a ser inserido?"))
if num1 >= 1:
    print("O número é positivo!.")
else:
    if num1 < 0:
        print("O número é negativo!")
    else:
        if num1 == 0:
            print("O seu numero é neutro")