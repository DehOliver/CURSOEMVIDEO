num_1 = float(input("Digite um primeiro valor: "))
num_2 = float(input("Digite um segundo valor: "))
num_3 = float(input("Digite um terceiro valor: "))
'''numero_maior = num_1 >= num_2 or num_3
numero_menor = int(num_1 <= num_2 or num_3)
print(numero_maior)
print(numero_menor)'''

if num_1 >= num_2 or num_3:
    print("O múmero {} é o maior.".format(num_1))
elif num_2 >= num_1 or num_3:
    print("O número {} é o maior.".format(num_2))
else:
    print("O número {} é o maior.".format(num_3))

if num_1 <= num_2 or num_3:
    print("O número {} é o menor.".format(num_1))
elif num_2 <= num_1 or num_3:
    print("O número {} é o menor.".format(num_2))
else:
    print("O número {} é o menor.".format(num_3))
