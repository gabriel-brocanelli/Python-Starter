casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salario * 30/ 100
if prestação <= mínimo:
    print('\033[32m Empréstimo pode ser CONCEDIDO!\033[m')
else:
    print('\033[31m Empréstimo NEGADO!\033[m')
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos))
print('a prestação será de R${:.2f}'.format(prestação))