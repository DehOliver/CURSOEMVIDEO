frase = str(input("Digite uma frase: "))

print("A Letra 'A' aparece {} vezes.".format(frase.lower().count("a")))
print("A Letra 'A' aparece pela primeira vez na posição {}.".format(frase.strip().find("a")))
print("A Letra 'A' aparece pela ultima vez na posição {}.".format(frase.strip().rfind("a")))