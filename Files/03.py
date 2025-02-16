# 3- Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

print('__________Feminino..._Masculino..._oq?__________')

sexo = input('Escreva o sexo (F ou M): ')

print('_________________________')

if (sexo == 'F'):
    print('O sexo é Feminino')
elif (sexo == 'M'):
    print('O sexo é Masculino')
else:
    print('Sexo inválido')