name = str(input("Digite seu nome completo: ")).strip()
divide_name = name.split()

print("Seu nome em maiúsculas é {}.".format(name.upper()))
print("Seu nome em minusculas é {}.".format(name.lower()))
print("Seu nome tem ao todo {} letras.".format(len(name) - name.count(" ")))
print("Seu primeiro nome é {} e ele tem {} letras.".format(divide_name[0], len(divide_name[0])))