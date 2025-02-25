exp = str(input('digite uma expressão:'))
lala = ''
lulu = ''
for la in exp:

    if la[0] == '(':
        if la == '(':
         lala += la
    elif la == ')':
        lulu += la
    else:
        break
print(lala)
if len(lala) == 0:
    print('Sua expressão esta errada')
elif len(lala) == len(lulu):      
    print('Sua expressão esta correta')
else:
    print('Sua expressão esta errada')

