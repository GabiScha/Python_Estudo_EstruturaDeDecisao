# 8- Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.

print('__________3_Produtos__________')

produto1 = int(input('Escreva o primeiro produto: '))
produto2 = int(input('Escreva o segundo produto: '))
produto3 = int(input('Escreva o terçeiro produto: '))


print('_________________________')

if (produto1 < produto2) and (produto1 < produto3):
    print(f'O primeiro numero ({produto1}) é o menor')
elif (produto2 < produto1) and (produto2 < produto3):
    print(f'O segundo numero ({produto2}) é o menor')
else:
    print(f'O terçeiro numero ({produto3}) é o menor')


