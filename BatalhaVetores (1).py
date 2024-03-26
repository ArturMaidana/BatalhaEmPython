#Alunos: Gustavo Capistrano e Artur Guilherme
import random

n_jogadores = int(input("Quantos jogadores irão jogar? (minimo 2)"))
m_rodadas = int(input("Quantas rodadas ? (Minimo 2)"))

if m_rodadas < 3:
  print("Número de rodadas inválido")
  exit()
if n_jogadores < 2:
  print("Número de jogadores inválido")
  exit()

nomes = []
for count in range(n_jogadores):
  nome = input(f"digite o nome do jogador {count + 1}: ")
  nomes.append(nome)

tabela = [[0] * m_rodadas for _ in range(n_jogadores)]
total_jogador = [0] * n_jogadores
melhor = 0

for j in range(m_rodadas):
  print(f"Rodada {j}: ", end='')

  for i in range(n_jogadores):
    tabela[i][j] = random.randint(0, 9)
    total_jogador[i] += tabela[i][j]

    if total_jogador[i] > melhor:
      melhor = total_jogador[i]

    print(f"Jogador {nomes[i]}: {tabela[i][j]}", end=' ')

print("\nTOTAL PARCIAL: ", end='')
for w in range(n_jogadores):
  print(f"Jogador {nomes[w]}: {total_jogador[w]}", end=' ')

print("\nDigite um caractere para continuar: ")
_ = input()

print("RESULTADO FINAL: ", end='')
for z in range(n_jogadores):
  if total_jogador[z] == melhor:
    print(f"Jogador {nomes[z]}: {total_jogador[z]}", end=' ')
  else:
    print(f"Jogador {nomes[z]}: {total_jogador[z]}", end=' ')
