"""Desenvolver um programa que pergunte um valor numérico inteiro e faça a exibição desse valor caso seja
divisível por 4 e 5. Não sendo divisível por 4 e 5, o programa deverá exibir a mensagem “Valor não é divisível por
4 e 5”"""

dig = int(input("Digite um valor numérico inteiro: "))


if dig % 4 == 0 and dig % 5 == 0:
    print(f"O valor {dig} é divisível por 4 e 5.")
else:
    print(f"O valor {dig} não é divisível por 4 e 5.")