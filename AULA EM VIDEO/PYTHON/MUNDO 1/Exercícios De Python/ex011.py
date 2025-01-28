lar = float(input('Qual a largura da sua parede? '))
alt = float(input('Qual a altura da parede? '))
mq = lar * alt
tin = mq / 2

print('A sua parede tem {}m², sendo necessário {}L de tinta para completar a pintura.'.format(mq, tin))