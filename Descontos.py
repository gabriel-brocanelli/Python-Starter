n1 = float(input('Qual é o preço do produto? R$ '))
desconto = n1 - (n1 * 5 / 100)
print('O produto que custava {:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(n1,desconto))