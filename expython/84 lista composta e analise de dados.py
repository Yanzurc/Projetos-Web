gale = []
tudo = []
esc = ''
pm = 0
pmn = []
pn = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
pnn = []
while esc != 'N':
    gale.append(str(input('Qual seu nome?:')))
    gale.append(int(input('Qual seu peso?:')))
    tudo.append(gale[:])
    if gale[1] == pm:
        pmn += gale[0]
    if gale[1] > pm:
        pm = gale[1]
        pmn = gale[0]
    if gale[1] == pn:
       pnn += gale[0]
    if gale [1] < pn:
       pn = gale [1]
       pnn = gale[0]
    esc = str(input('Você deseja continuar? [S/N]')).upper()
    gale.clear()
print(f'O total de pessoas cadastradas foram {len(tudo)}')
print(f'O maior peso foi {pm}Kg. Peso de {pmn}')
print(f'o menor peso foi {pn}Kg. Peso de {pnn}')