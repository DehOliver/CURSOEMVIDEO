from time import sleep

num = int(input("Digite um número inteiro: "))
print("Analisando...")
sleep(2)
if num % 2 == 0:
    print("O número {} é par.".format(num))
else:
    print("O número {} é ímpar.".format(num))