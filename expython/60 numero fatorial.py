print('digite um numero para')
num = int(input('descobrirmos seu fatorial: '))
fac = num
a = num
while fac > 1:
    fac -= 1
    a *= fac
    #print(fac, a, end=' ')
print('o fatorial de {} e {}'.format(num, a))

