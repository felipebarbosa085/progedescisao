"""Fazer um algoritmo que pergunte a idade de uma pessoa, e ao final, informe na tela se a pessoa é menor de
idade, se é maior de idade, ou se é maior de 65 anos.
"""

idd = int(input("Digite a idade da pessoa: "))

if idd < 18:
    print("A pessoa é menor de idade.")

elif idd >= 18 and idd <= 65:
    print("A pessoa é maior de idade.")
else:
    print("A pessoa é maior de 65 anos.")