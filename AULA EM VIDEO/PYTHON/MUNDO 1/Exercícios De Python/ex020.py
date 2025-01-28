from random import shuffle


al1 = str(input("Quem é o primeiro aluno? "))
al2 = str(input("Quem é o segundo aluno? "))
al3 = str(input("Quem é o terceiro aluno? "))
al4 = str(input("Quem é o quarto aluno? "))
lista = [al1, al2, al3, al4]
shuffle(lista)

print("A ordem de apresentação será:\n{}".format(lista))