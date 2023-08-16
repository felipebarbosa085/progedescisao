"""Fazer um algoritmo que pergunte 3 números, e ao final, guarde na variável maior o maior destes 3 números
inseridos. O valor da variável maior deverá ser exibido ao final."""

num1 = int(input("Qual o numero a ser inserido?"))
num2 = int(input("Qual o numero a ser inserido?"))
num3 = int(input("Qual o numero a ser inserido?"))

maior = num1

if maior < num2:
    maior = num2

if maior < num3:
    maior = num3

    print("O maior valor dentre os números inserido é", maior)