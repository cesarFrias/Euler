condicao = True
j = 1
while condicao:
    if any(j % i for i in xrange(1, 21)) == False:
        condicao = False
    else:
        j += 1
print j
