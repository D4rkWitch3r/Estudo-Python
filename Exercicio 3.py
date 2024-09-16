import random
ordem = []
for i in range(4):
    alunos = input("Infome o nome dos alunos:")
    ordem.append(alunos)
sorteio = random.shuffle(ordem)
print(f"A ordem de apresentação será: {ordem}")