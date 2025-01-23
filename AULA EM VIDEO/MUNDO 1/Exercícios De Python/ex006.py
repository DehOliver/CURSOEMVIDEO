n = int(input('Digite um valor: '))
d = n * 2
t = n * 3
r = n**(1/2)

print('Seu valor escolhido é {}, o dobro dele é {}, o triplo dele é {} e sua raiz quadrada é {:.2f}!'.format(n, d, t, r))
print('=================================')
print('Seu valor escolhido é {}. \nO dobro de {} é {}. \nO triplo de {} é {}. \nA raiz quadrada de {} é {:.2f}.'.format(n, n, d, n, t, n, r))
print('=================================')
print('Seu valor escolhido é {}. \nO dobro de {} é {}. \nO triplo de {} é {}. \nA raiz quadrada de {} é {:.2f}.'.format(n, n, (n*2), n, (n*3), n, (n**(1/2))))