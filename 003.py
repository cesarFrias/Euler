from math import sqrt
numero = 600851475143
for i in xrange(1, int(sqrt(numero))):
    if numero % i == 0:
        maior_divisor = i
        numero = numero / i
print maior_divisor
