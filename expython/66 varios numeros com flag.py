num = soma =cont = 0
while num != 999:

    num = int(input('Digite um valor [se quiser parar digite 999]: '))
    if num == 999:
        break
    else:
        soma += num
        cont += 1
print(f'Você digitou {cont} valores, e a soma entre eles é {soma}')