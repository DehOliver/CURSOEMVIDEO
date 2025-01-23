import math

num_1 = float(input("Digite o Valor do ângulo que deseja calcular: "))
seno = math.sin(num_1)
cosseno = math.cos(num_1)
tangente = math.tan(num_1)

print("O Ângulo de {} tem o Seno de {}°, o Cosseno de {}° e a Tangente de {}°.".format(num_1, seno, cosseno, tangente))