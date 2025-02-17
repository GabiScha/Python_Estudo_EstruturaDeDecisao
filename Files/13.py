#13- Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

print('__________Dias_da_semana__________')


dia = int(input('Por favor escreva o dia da semana: '))

print('_________________________')


if dia < 1 or dia > 7:
    print('Valor incorreto')
elif dia == 1:
    print('Domingo')
elif dia == 2:
    print('Segunda')
elif dia == 3:
    print('Terça')
elif dia == 4:
    print('Quarta')
elif dia == 5:
    print('Quinta')
elif dia == 6:
    print('Sexta')
else:
    print('Sábado')

