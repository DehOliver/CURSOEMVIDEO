import math

num_1 = float(input("Digite o valor do Cateto Oposto: "))
num_2 = float(input("Digite o valor do Cateto Adjacente: "))
soma = math.pow(num_1, 2) + math.pow(num_2, 2)
raiz = soma
hipo = math.sqrt(raiz)
print("Com a soma do Cateto Oposto ({}) com o Cateto Adjacente ({}), o resultado da Hipotenusa é {:.2f}.".format(num_1, num_2, hipo))