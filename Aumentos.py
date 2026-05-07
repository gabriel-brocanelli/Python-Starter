n1 = float(input('Qual o salário di Funcionário? R$ '))
aumento = n1 + (n1 * 15 / 100)
print('Um funcionário que ganhava R${} , com 15% de aumento, passa a receber R${:.2f}'.format(n1,aumento))
