nums = []
num = []
par = maior2 = col3 = 0
for c in range(1, 10):
    num.append(int(input(f'Digite o {c}º digito')))
    nums.append(num[:])
    if num[0] % 2 == 0:
        par += num[0]
    if c == 3 or c == 6 or c == 9:
        col3 += num[0]
    if c >= 4 and c <= 6:
        if num[0] >  maior2:
            maior2 = num[0]
    num.clear()
print('=-=' * 15)
print(f'[ {nums[0]} ]  [ {nums[1]} ]  [ {nums[2]} ]\n[ {nums[3]} ]  [ {nums[4]} ]  [ {nums[5]} ]\n[ {nums[6]} ]  [ {nums[7]} ]  [ {nums[8]} ]')
print(f'A soma dos pares foram {par}')
print(f'A soma dos numeros da terceira coluna foram {col3}')
print(f'O maior da segunda linha foi {maior2}')