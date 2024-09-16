valor = float(input('Me diga o valor do produto R$'))
desconto1 = valor - (valor*10)/100
desconto2 = valor - (valor*5)/100
if valor >=100:
    print(f'O valor do produto com o desconto ficou \033[0;31mR${desconto1:.2f}\033[m')
else:
    print(f'O valor do produto com o desconto ficou R${desconto2:.2f}')