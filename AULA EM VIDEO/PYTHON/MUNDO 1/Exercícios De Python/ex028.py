import random
import time
print("-=-" * 20)
print("Escolhendo um número entre 0 e 10...")
print("-=-" * 20)
random_number = random.randint(0, 10)
time.sleep(2)

user_choice = print(input("O número foi escolhido! Tente acertar minha decisão: "))
if user_choice == random_number:
    print("Parabéns! Você acertou! (Não trapaceou né?)")
else:
    print("Você errou! O número era {}, agora eu sou o dono deste dispositivo!".format(random_number))   
    