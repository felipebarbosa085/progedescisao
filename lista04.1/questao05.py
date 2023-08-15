"""Desenvolver um programa que pergunte 4 notas escolares de um aluno e exiba mensagem informando que o
aluno foi aprovado se a média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma
mensagem informando essa condição. Apresentar junto com a mensagem de aprovação ou reprovação o valor
da média obtida pelo aluno"""

num1 = float(input("Qual a sua primeira nota?"))
num2 = float(input("Qual a sua segunda nota?"))
num3 = float(input("Qual a sua terceira nota?"))
num4 = float(input("Qual a sua quarta nota?"))

notal = num1 + num4 + num3 + num2
res = notal/4

if (res <=5):
    print(f"{notal} Voce esta reprovado!")

else:
    if (res>5):
        print(f"{res}Voce esta aprovado! ")
