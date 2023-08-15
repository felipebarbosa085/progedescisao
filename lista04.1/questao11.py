""" Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado
somente o algarismo das centenas."""

num1 = int(input("Digite um número inteiro de 3 algarismos: "))
if 100 <= num1 <= 999:
    cent = num1 // 100
    print("O algarismo das centenas é:", cent)
else:
    print("O número não possui 3 algarismos.")
