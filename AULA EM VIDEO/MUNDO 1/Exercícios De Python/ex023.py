from time import sleep


num = int(input("Digite um número: "))
n = str(num)

print("Analisando seu número...")
sleep(2.00)

print("Analisando o número {}.\n Unidade: {}\n Dezena: {}\n Centena: {}\n Milhar: {}".format(num, n[3], n[2], n[1], n[0]))