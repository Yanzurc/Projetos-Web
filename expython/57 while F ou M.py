sex = ''
while sex != 'F' and sex != 'M':
    sex = str(input('Qual e o seu sexo? [M\F]: ')).upper()
if sex == 'M':
    print('Entâo você e um homem, prazer em te conhcer.')
else:
    print('Então você e uma mulher, prazer em te conhecer')