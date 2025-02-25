alunos = []
aluno = []
media = []
medias = []
cont = 0
while True:
    aluno.append(str(input('NOME:')))
    aluno.append(float(input('NOTA1:')))
    aluno.append(float(input('NOTA2:')))
    alunos.append(aluno[:])
    media.append((aluno[1] + aluno[2]) / 2)
    print(media)
    medias.append(media[:])
    aluno.clear()
    media.clear()
    esc = str(input('Deseja adicionar mais algum aluno? [S/N]: ')).upper()
    if esc == 'N':
        break
print('==' * 20)
print('            NOTA DOS ALUNOS')
print('--' * 20)
for c in range(0, len(alunos)):
    print(f'{alunos[cont][0]}')
    cont += 1
print('==' * 20)