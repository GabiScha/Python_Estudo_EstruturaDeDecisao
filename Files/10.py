# 10- Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


print('__________Bom_Dia__________')

hr = input('Por favor escreva em qual turno vc estuda: ')

if hr == 'M':
    print('Bom Dia!')
elif hr == 'V':
    print('Boa Tarde!')
elif hr == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido!')

    