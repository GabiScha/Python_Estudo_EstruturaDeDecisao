#12- Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00  
#         (-) INSS (10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00


print('__________Folha_de_pagamento__________')


salario = int(input('Escreva o salário: '))

print('_________________________')


if salario <= 0:
    print('Algo de errado não está certo')
elif salario <= 900:
    salario_liquido = salario - (((salario / 100) * 11)) + (((salario / 100) * 0) + ((salario / 100) * 10))
    print(f'+ Salário Bruto : R$ {salario}\n+ IR (0%): R${00}\n+ INSS (10%): R${(salario / 100) * 10}\n- FGTS (11%)  : R${((salario / 100) * 11)}\n= Total de descontos: R${(salario / 100) * 10 + ((salario / 100) * 0) }\n= Salário Liquido: R${salario_liquido}')
elif salario <= 1500:
    salario_liquido = salario - (((salario / 100) * 11)) + (((salario / 100) * 5) + ((salario / 100) * 10))
    print(f'+ Salário Bruto : R$ {salario}\n+ IR (5%): R${((salario / 100) * 5)}\n+ INSS (10%): R${(salario / 100) * 10}\n- FGTS (11%)  : R${((salario / 100) * 11)}\n= Total de descontos: R${(salario / 100) * 10 + ((salario / 100) * 5) }\n= Salário Liquido: R${salario_liquido}')
elif salario <= 2500:
    salario_liquido = salario - (((salario / 100) * 11)) + (((salario / 100) * 10) + ((salario / 100) * 10))
    print(f'+ Salário Bruto : R$ {salario}\n+ IR (10%): R${((salario / 100) * 10)}\n+ INSS (10%): R${(salario / 100) * 10}\n- FGTS (11%)  : R${((salario / 100) * 11)}\n= Total de descontos: R${(salario / 100) * 10 + ((salario / 100) * 10) }\n= Salário Liquido: R${salario_liquido}')  
elif salario > 2500:
    salario_liquido = salario - (((salario / 100) * 11)) + (((salario / 100) * 20) + ((salario / 100) * 10))
    print(f'+ Salário Bruto : R$ {salario}\n+ IR (20%): R${((salario / 100) * 20)}\n+ INSS (10%): R${(salario / 100) * 10}\n- FGTS (11%)  : R${((salario / 100) * 11)}\n= Total de descontos: R${(salario / 100) * 10 + ((salario / 100) * 20) }\n= Salário Liquido: R${salario_liquido}')          



