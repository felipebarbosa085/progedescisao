"""Fazer um algoritmo que pergunte o ano de nascimento de uma pessoa e o ano atual. Ao final o algoritmo
deverá exibir na tela a idade da pessoa. Porém, se o usuário inserir o ano de nascimento com valor maior
que o ano atual, o cálculo de idade não deverá ser feito, e então deverá surgir a seguinte mensagem na tela:
“Dados inseridos estão incorretos”."""

idd = int(input("Informe o ano em que você nasceu:"))
ano = int(input("Informe o ano em que nós estamos:"))
idade = ano - idd

if (ano > 2024):
    print(f" Dados inseridos estão incorretos")

else:
    print(f"voce tem", idade,"anos!")
