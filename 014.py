num_inicial_tam = []

def calcula_proximo_numero(numero):
    if numero % 2 == 0:
        return numero / 2
    else:
        return (3 * numero) + 1

for i in xrange(1, 1000000):
    sequencia = []
    sequencia.append(i)
    while sequencia[-1] > 1:
        sequencia.append(calcula_proximo_numero(sequencia[-1]))
    num_inicial_tam.append([i, len(sequencia)])

num_inicial_tam.sort(key=lambda num_tam: num_tam[1], reverse=True)
print num_inicial_tam[0]
