""" Desenvolver um programa que pergunte dois números inteiros, e apresente como resultado se o segundo
número informado é ou não um divisor do primeiro número informado."""

num1 = int(input("Qual o numero a ser inserido?"))
num2 = int(input("Qual o numero a ser inserido?"))

if (num2%num1):
    print("O seu numero é divisor")
else:
    print("O seu numero não é divisor")

print("FIM DO PROGRAMA")
