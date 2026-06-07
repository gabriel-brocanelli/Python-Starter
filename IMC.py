peso = float(input('Qual é seu peso: '))
altura = float(input('Qual é sua altura: '))
imc = peso / (altura **2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal! ')
elif imc >= 18.5 and imc < 25:
    print('Você está no PESO IDEAL!')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE!')
elif imc >= 40:
    print('Você está com OBESIDADE MÓRBIDA!')