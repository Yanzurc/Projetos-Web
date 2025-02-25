tudo = 0
impar = []
par = []
for c in range(1, 8):
  tudo=(int(input(f'Digite o {c}º numero:')))
  if tudo % 2 == 0:
      par += [tudo]
  else:
      impar += [tudo]
print(f'pares{sorted(par)}\nimpares{sorted(impar)}')