a = float(input("Digite o valor da primera reta: "))
b = float(input("Digite o valor da segunda reta: "))
c = float(input("Digite o valor da terceira reta: "))

if a + b > c and c + b > a and a + c > b:
    print("É possivel fazer um triangulo com essas retas!")
else:
    print("Infelizmente essas retas não conseguem formar um triangulo.")
