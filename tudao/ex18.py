from math import hypot
co = float(input('qual o comprimento do cateto oposto? '))
ca = float(input('e do cateto adjacente? '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))


