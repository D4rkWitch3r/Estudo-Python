import random

times = []

print("Vamo disputar uma partida de futebol, infome ao programa os times!!!!")

t1 = input("Me diga o primeiro time: ")
times.append(t1)

t2 = input("Me diga o segundo time: ")  
times.append(t2)

time1 = 0
time2 = 0

max = int(input("Informe o máximo de gols que pode acontecer na partida:"))

while time1 + time2 <= max:

    usuario = random.choice(times)
    if usuario == t1:
        time1 += 1
        print (f"O Jogo está {t1} {time1} vs {t2} {time2}")
        
    elif usuario == t2:
        time2 += 1
        print (f"O Jogo está {t2} {time2} vs {t1} {time1}")

print(f"O jogo acabou e ficou {t1} {time1} & {t2} {time2}")



  




