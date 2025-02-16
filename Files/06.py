# 6- Faça um Programa que leia três números e mostre o maior deles.


print('__________Maior_Ⅱ__________')

num1 = int(input('Escreva o primeiro número: '))
num2 = int(input('Escreva o segundo número: '))
num3 = int(input('Escreva o terçeiro número: '))

print('_________________________')

if (num1 > num2) and (num1 > num3):
    print(f'O primeiro numero ({num1}) é o maior')
elif (num2 > num1) and (num2 > num3):
    print(f'O segundo numero ({num2}) é o maior')
else:
    print(f'O terçeiro numero ({num3}) é o maior')


