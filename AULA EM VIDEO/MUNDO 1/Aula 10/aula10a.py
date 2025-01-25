"""nome = str(input("Qual é o seu nome? "))
if nome == "Denner":
    print("Que nomezinho dificil, hein menino!")
else:
    print("Seu nome é simples, graças a Zeus!")
print("Buenas seras, {}!".format(nome))"""

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
media = (n1 + n2 + n3)/ 3

print("As notas foram {:.1f}, {:.1f} e {:.1f} e a média é {:.2f}.".format(n1, n2, n3, media))
if media >= 16:
    print("Parabéns, você passou com louvor no vestibular!")
else:
    print("Infelizmente você não alcançou a média necessária pra passar no vestibular.")