#11- As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#      Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.


print('__________Tabajara__________')


salario = int(input('Escreva o salário: '))

print('_________________________')

if salario <= 280:
    fim = salario + (salario / 100) * 20
    per = '20%'
elif salario > 280 and salario <= 700:
    fim = salario + (salario / 100) * 15
    per = '15%'
elif salario > 700 and salario < 1500:
    fim = salario + (salario / 100) * 10
    per = '10%'
elif salario > 1500:
    fim = salario + (salario / 100) * 5
    per = '5%'


print(f'O salario antes do reajuste era R${salario}')
print(f'Aumentou: {per}')
print(f'Aumentou: R${fim - salario}')
print(f'O salário final foi: R${fim}')
