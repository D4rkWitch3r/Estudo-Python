import random
alunos = []
for i in range(4):
    aluno = input('Digite o nome dos alunos:')
    alunos.append(aluno)
sorteio = random.choice(alunos)
print(f'O aluno sorteado foi: {sorteio}')
