""" Fazer um algoritmo que peça um número, e ao final, informe se o número digitado está acima de 1000 ou
abaixo de 1000."""

num1 = int(input("Digite um número inteiro: "))
if 999 <= num1 >= 1000:
    print("O seu numero está acima de 1000:")
else:
    print("O seu numero está abaixo de 1000.")