"""Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste."""

num = (input("Digite a sigla de um estado brasileiro "))

if num == "MG":
    print("O seu estado esta na região sudeste!")
elif num == "ES":
    print("O seu estado esta na região sudeste")
elif num == "SP":
    print("O seu estado esta na região sudeste")
elif num == "RJ":
    print("O seu estado esta na região sudeste")
else:
    print("Esse estado ou unidade federativa não está no sudeste")



