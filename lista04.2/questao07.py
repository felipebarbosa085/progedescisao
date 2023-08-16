"""Fazer um algoritmo que pergunte 2 números, e ao final, exiba como resposta na tela qual é o maior e qual é
o menor, ou ainda, se ambos são iguais."""

numero1 = float(input("Escreva um número:"))
numero2 = float(input("Escreva o segundo número:"))

if numero1 == numero2:
    print("Os números são iguais.")
elif numero1 > numero2:
    print(f"O maior número é: {numero1}")
    print(f"O menor número é: {numero2}")
else:
    print(f"O maior número é: {numero2}")
    print(f"O menor número é: {numero1}")
