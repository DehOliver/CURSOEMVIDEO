from time import sleep

city = str(input("Digite o nome da cidade onde você nasceu: ")).strip()

print("Analisando cidade informada...")
sleep(2.00)

print("A sua cidade possui o nome inicial de Santo? {}".format(city[:5].upper() == "SANTO"))