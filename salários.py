fun = float(input('Informe seu salário R$'))
aum1 = fun + (fun*10)/100
aum2 = fun + (fun*15)/100
if fun >=1250:
    print(f"O seu aumento foi de R${aum1:.2f}")
else:
    print(f'O seu aumento foi de R${aum2:.2f}')