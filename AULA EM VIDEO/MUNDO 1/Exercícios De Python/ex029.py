from time import sleep

velocidade = float(input("Qual a velocidade atual do carro? "))
sleep(1)
print("Verificando limite da via...")
sleep(2)
if velocidade > 90:
    print("Atenção! Você excedeu o limite de velocidade permitido! Você foi multado.")
    multa = (velocidade - 90) * 7 #Gera 7 reais de multa por Km excedido.
    print("O valor da sua multa é de R${:.2f}, Pague em dia para evitar inadimplêmcia.".format(multa))
else:
    print("Mantenha-se seguro e siga viagem!")