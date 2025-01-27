salario = float(input("Qual o valor do seu salário atual? "))

if salario <=1250:
    aumento = (15 * salario) / 100
else:
    aumento = (10 * salario) / 100

print("Com o aumento< seu salário subiu de {:.1f} para {:.1f}!".format(salario, salario+aumento))