prc = float(input('Qual o valor do produto: '))
desc = prc * 5
descf = desc / 100
vlrf = descf - prc


print('O valor final do seu produto com 5%'' de desconto ficou R${:.2f}.'.format(abs(vlrf)))