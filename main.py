DESCONTO_10 = 10
DESCONTO_20 = 20
DESCONTO_30 = 30
DESCONTO_50 = 50

valor_conta = float(input('Qual o valor da conta? '))

valor_10 = valor_conta <= 1000
valor_20 = valor_conta > 1000 and valor_conta <= 5000
valor_30 = valor_conta > 5000 and valor_conta <= 10000

if valor_10:
    valor_total = valor_conta - (valor_conta * (DESCONTO_10 / 100))
    print(f'Valor total com desconto de 10% a ser pago: {valor_total:.2f}')
elif valor_20:
    valor_total = valor_conta - (valor_conta * (DESCONTO_20 / 100))
    print(f'Valor total com desconto de 20% a ser pago: {valor_total:.2f}')
elif valor_30:
    valor_total = valor_conta - (valor_conta * (DESCONTO_30 / 100))
    print(f'Valor total com desconto de 30% a ser pago: {valor_total:.2f}')
else:
    valor_total = valor_conta - (valor_conta * (DESCONTO_50 / 100))
    print(f'Valor total com desconto de 50% a ser pago: {valor_total:.2f}')
