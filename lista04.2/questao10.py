"""Fazer um algoritmo que pergunte o nome do aluno, e as notas das provas 1 e 2. Deverá ser exibida na tela
como resposta a média do aluno, e se ele está aprovado, reprovado ou em prova final. Estas condições
devem seguir as regras da tabela abaixo:"""

aluno = input("Qual o nome do aluno?")
nota1 = float(input("Digite a nota da prova 1: "))
nota2 = float(input("Digite a nota da prova 2: "))

media = (nota1 + nota2) / 2

if (media < 3):
     print("Você está reprovado! sua média é de",media)
else:
    if(media <= 6.9):
      print(f" Você está em prova final! sua média é de", media)
    else:
     print(f"Você está aprovado! sua média é de", media)


