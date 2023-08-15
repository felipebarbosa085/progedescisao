"""Desenvolver um programa que pergunte um número. Se este número for maior que 20, então ele deverá exibir a
metade deste número, senão, ele deverá exibir o número sem alterações"""

num1 = int(input("Qual o numero a ser inserido?"))

if (num1 < 20):
    print("O seu numero é", num1/2)
else:
    print("o seu numero sem alterações é",num1)

print("FIM DO PROGRAMA")

