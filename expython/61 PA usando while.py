pri = int(input('digite o primeiro numero: '))
ra = int(input('digite a razão: '))
dez = pri + (10 - 1) * ra
pa = pri
while pa < dez + ra:
    print('{},'.format(pa), end=' ')
    pa += ra