import math

num_1 = float(input("Digite o Valor do ângulo que deseja calcular: "))
seno = math.sin(math.radians(num_1))
cosseno = math.cos(math.radians(num_1))
tangente = math.tan(math.radians(num_1))

print("O Ângulo de {} tem o Seno de {:.2f}°, o Cosseno de {:.2f}° e a Tangente de {:.2f}°.".format(num_1, seno, cosseno, tangente))