n1 = float(input('Quanto de dinheiro você tem na carteira? R$'))
print('Com R${} você pode comprar US${:.2f} '.format(n1,(n1/4.95)))
print('Com R${} você pode comprar EUR${:.2f} '.format(n1,(n1 / 5.80)))
# dolar = n1 / 4.95
# euro = n1 / 5.80