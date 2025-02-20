# 16- Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
import math

print('__________Equação_2°_Grau__________')


a = int(input('Por favor digite o a: '))

if (a != 0):
    b = int(input('Por favor digite o b: '))
    c = int(input('Por favor digite o c: '))

    delta = b**2 - (4*a*c)

    if delta < 0:
        print('-------------------------')
        print('A equação não possui raizes reais!.')
    elif delta == 0:
        raiz = -b / (2*a)
        print('-------------------------')
        print(f'A equação equação possui apenas uma raiz real que é {raiz}.')
    else:
        raizDelta = math.sqrt(delta)
        x1 = (-b + raizDelta) / (2*a)
        x2 = (-b - raizDelta) / (2*a)
        print('-------------------------')
        print(f'A equação equação possui 2 raizes reais, que são: x1({x1}) e x2({x2}).')

else:
    print('-------------------------')
    print(f'A equação não é de segundo grau!')





