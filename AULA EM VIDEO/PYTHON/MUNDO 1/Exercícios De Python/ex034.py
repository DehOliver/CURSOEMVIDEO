salario = float(input("Qual o valor do seu salário atual? R$ "))

if salario <=1250:
    aumento = (15 * salario) / 100
else:
    aumento = (10 * salario) / 100

print("Com o aumento< seu salário subiu de R${:.2f} para R${:.2f}!".format(salario, salario+aumento))