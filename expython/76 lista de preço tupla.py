tabelinha = 'Lapis', 0.50, 'caneta', 1.00, 'borracha', 1.50, 'corretivo', 3.00, 'lapiseira', 4.50
print('==-' * 16)
print('                TABELA DE PREÇO')
print('==-' * 16)
ps = 0
for pos in range(0, 5):
    print(f' {tabelinha[ps]:.<38}', 'R$', end=' ')
    ps += 1
    print(f'{tabelinha[ps]:.2f}')
    ps += 1
print('==-' * 16)
