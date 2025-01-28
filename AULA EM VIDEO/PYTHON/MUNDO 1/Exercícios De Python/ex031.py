from time import sleep

travel = float(input("Qual a distância em quilômetros da sua viagem? "))
print("Analisando o percurso...")
sleep(1)
if travel <= 300:
    price = travel * 0.50
    print("O valor da sua passagem neste percurso é de R${:.2f}.".format(price))
else:
    price = travel * 0.45
    print("O valor da sua passagem neste percurso é de R${:.2f}.".format(price))