tutu = 'Yan', 'Cruz', 'de', 'Oliveira'
for psiu in tutu:
    print(f'No nome\sobrenome {psiu} contem as vogais:', end=' ')
    if 'a' in psiu:
        print('A', end=' ')
    if 'e' in psiu:
        print('E', end=' ')
    if 'i' in psiu:
        print('I', end=' ')
    if 'o' in psiu:
        print('O', end=' ')
    if 'u' in psiu:
        print('U', end=' ')
    print('')