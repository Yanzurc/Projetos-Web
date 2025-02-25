r = 0
print('==' * 21)
num = int(input('digite um numero: '))
num1 = int(input('digite outro numero: '))
while r != 5:
     list = [num, num1]
     print('-' * 42)
     print('[1] soma')
     print('[2] multiplicar')
     print('[3] maior')
     print('[4] novos numeros')
     print('[5] sair')
     r = int(input('Qual ação o senhor(A) vai efetuar?:'))
     if r == 1:
         print('{} + {} = {}'.format(num, num1, num + num1))
     if r == 2:
        print('{} * {} = {}'.format(num, num1, num * num1))
     if r == 3:
         print('entre os dois numero que você escolheu o maior e o numero {}'.format(max(list)))
     if r == 4:
         print('==' * 21)
         num = int(input('digite um numero: '))
         num1 = int(input('digite outro numero: '))

print('A tabela de opções foi finalizada')