mt = float(input('Quantos metros você quer converter?' ))
cm = mt * 100
mm = mt * 1000
km = mt / 1000
hm = mt / 100
dam = mt / 10
dm = mt * 10

print('Convertendo {}m, dá {}cm e {}mm!'.format(mt, cm, mm))
print('===========================================')
print('A medida de {}m corresponde a: \n{}Km, \n{}Hm, \n{}Dam, \n{}dm, \n{}cm, \n{}mm'.format(mt, km, hm, dam, dm, cm, mm))
