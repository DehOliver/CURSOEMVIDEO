num_1 = int(input("Digite um primeiro valor: "))
num_2 = int(input("Digite um segundo valor: "))
num_3 = int(input("Digite um terceiro valor: "))
'''numero_maior = num_1 >= num_2 or num_3
numero_menor = int(num_1 <= num_2 or num_3)
print(numero_maior)
print(numero_menor)'''

'''if num_1 >= num_2 or num_3:
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
    print("O número {} é o menor.".format(num_3))'''

if num_1>num_2 and num_1>num_3:
    maior = num_1
if num_2>num_1 and num_2>num_3:
    maior = num_2
if num_3>num_1 and num_3>num_2:
    maior = menor = num_3   

if num_1<num_2 and num_1<num_3:
    menor = num_1
if num_2<num_1 and num_2<num_3:
    menor = num_2
if num_3<num_1 and num_3<num_2:
    menor = num_3

print("O menor número é {}.".format(menor))
print("O maior número é {}.".format(maior))