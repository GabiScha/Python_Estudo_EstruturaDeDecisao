# 4- Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

print('__________Vogal_ou_Consoante__________')



num = 0
while num < 11: #assim da pra testar tds as possibilidades

    letra = input('Escreva a letra: ')

    print('_________________________')



    if (letra == 'a') or (letra == 'i') or (letra == 'u') or (letra == 'e') or (letra == 'o') or (letra == 'A' ) or (letra == 'I') or (letra == 'U') or (letra == 'E') or (letra == 'O'):
        print(f'A letra {letra} é vogal')
    else:
        print(f'A letra {letra} é consoante')
    num += 1