maior18 = 0
mans = 0
muie = 0
while True:
    idade = int(input('digite a sua idade:'))
    sexo = str(input('Qual e seu sexo [M\F]')).upper()
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        mans += 1
    if sexo == 'F' and idade <= 20:
        muie += 1
    escolha = str (input('Voce deseja adicionar mais alguem?. se sim digite S se não digite N: ')).upper()
    if escolha == 'N':
        break
print(f'Tem {maior18} com com mais de 18 anos')
print(f'{mans} homens foram registrados')
print(f'{muie} mulheres foram registrados com menos de 20 anos')

