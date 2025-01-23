rs = float(input('Quantos reais você tem atualmente? '))
cambio = rs / 3.27
usd = cambio


print('Com a taxa de câmbio de US$ 3,27, você converteu R${} e ficou com US${:.2f}'.format(rs, usd))
