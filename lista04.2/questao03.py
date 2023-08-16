"""Fazer um algoritmo que peça um número, e ao final, informe se o número está abaixo de 1000, entre 1000 e
5000, entre 5001 e 8000, ou acima de 8000."""

num = int(input("Informe um número: "))

if (num < 1000):
    print(f"{num} está abaixo de 100.")

else:
    if (num <= 1000):
        print(f"{num} está entre 1000 e 5000.")
    else:
        print(f"{num} está acima de 5000")
    if (num <=5001):
        print(f"{num} está entre de 5001 e 8000")
    else:
        print(f"{num} está acima de 8000")