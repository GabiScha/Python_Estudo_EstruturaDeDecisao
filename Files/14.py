#14- Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.


print('__________Notas__________')


nota1 = int(input('Escreva a primeira nota: '))
nota2 = int(input('Escreva a primeira nota: '))


print('_________________________')


media = (nota1 + nota2)/ 2

if media <= 10 and media >= 9:
    print('Sua nota é A')
elif media >= 7.5 and media < 9:
    print('Sua nota é B')
elif media >= 6.0 and media < 7.5:
    print('Sua nota é C')
elif media >= 4.0 and media < 6.0:
    print('Sua nota é D')
elif media >= 0 and media < 4.0:
    print('Sua nota é D')
else:
    print('Nota inválida')


