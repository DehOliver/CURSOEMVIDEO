from random import choice

al1 = str(input("Qual o nome do primeiro aluno? "))
al2 = str(input("Qual o nome do segundo aluno? "))
al3 = str(input("Qual o nome do terceiro aluno? "))
al4 = str(input("Qual o nome do quarto aluno? "))
lista = [al1, al2, al3, al4]
escolhido = choice(lista)

print("O aluno escolhido para a tarefa foi {}.".format(escolhido))