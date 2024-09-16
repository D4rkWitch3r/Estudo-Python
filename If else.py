import random
sorteio = random.randint(0,5)
usuario = int(input("Informe um núemro de 1 a 5: "))
if usuario == sorteio:
    print (f'Você venceu!!!!\n o computador escolheu: {sorteio}')
else:
    print (f'O computador venceu, tente novamente!!!!\n o computador escolheu: {sorteio}')