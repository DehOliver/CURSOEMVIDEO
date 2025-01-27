from time import sleep

ano = int(input("Digite um ano: "))
print("Analisando o ano...")
sleep(2)

if ano % 4 == 0:
  print("O ano de {} é bissexto.".format(ano))
elif ano % 400 == 0:
  print("O ano de {} é bissexto.".format(ano))
else:
  print("O ano de {} não é bissexto.".format(ano))