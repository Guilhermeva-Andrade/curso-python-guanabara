import math
a = float(input('Digite um ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O seno de {} é {}, o coseno de {} e a tangente {}'.format(a, s, c, t))
