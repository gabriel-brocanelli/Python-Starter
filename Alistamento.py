from datetime import date
ano_atual = date.today().year
genero = input('Qual o seu gênero? (homem/mulher): ').strip().lower()
ano_nascimento = int(input('Ano de nascimento: '))

idade = ano_atual - ano_nascimento
print('-' * 40)
if genero == 'homem':
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nascimento,idade,ano_atual))
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = idade - 18
        ano_alistamento = ano_atual + saldo
        print('Ainda faltam {} anos para o alistamento.'.format(saldo))
        print('Seu alistamento será em {}. '.format(ano_alistamento))
    else:
        saldo = idade - 18
        ano_alistamento = ano_atual - saldo
        print('Você ja deveria ter se alistado há {} anos'.format(saldo))
        print('Seu alistamento foi em {}.'.format(ano_alistamento))
elif genero == 'mulher':
    print('Você não precisa fazer o alistamento obrigatorio!')
else:
    print('Opção invalida. Escolha um dos gêneros a cima!')
