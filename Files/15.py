# 15- Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;



print('__________Triangulo__________')


lado1 = int(input('Por favor digite o primeiro lado: '))
lado2 = int(input('Por favor digite o segundo lado: '))
lado3 = int(input('Por favor digite o terçeiro lado: '))


print('-------------------------')
       

if (lado1 == lado2) and (lado2 == lado3):
    print('Triângulo Equilátero')
elif (lado1 == lado2) or (lado2 == lado3) or (lado3 == lado1):
    print('Triângulo Isósceles')
else:
    print('Triângulo Escaleno')


