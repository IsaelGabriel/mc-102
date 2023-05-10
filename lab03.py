n_jogadores = int(input()) # Número de jogadores (J, como descrito no exercício)
n_caixa = [int(i) for i in input().split(" ", n_jogadores)] # Números retirados da caixa por jogadores
limites_intervalos = [int(i) for i in input().split(" ", n_jogadores*2)] # Limites dos intervalos dos jogadores
intervalos = [[limites_intervalos[i],limites_intervalos[i+1]] for i in range(0,len(limites_intervalos),2)] # Lista com os intervalos dos jogadores representados em listas

primeira_metade = 0 # Quantidade de jogadores na primeira metade

if n_jogadores % 2 == 0:
    primeira_metade = n_jogadores // 2
else:
    primeira_metade = (n_jogadores + 1) // 2

pontuacoes = [] # Lista de pontuações dos jogadores

for i in range(0,n_jogadores):
    if i < primeira_metade: # Se jogador atual se encontra na primeira metade da lista
        pontuacoes.append((intervalos[i][1]-intervalos[i][0])*n_caixa[i])
    else: # Se o jogador atual se encontra na segunda metade da lista
        pontuacoes.append((intervalos[i][1]-intervalos[i][0])+n_caixa[i])

pontuacoes_ordenadas = [] # Lista das pontuações dos jogadores em ordem não decrescente
pontuacoes_ordenadas = pontuacoes.copy()
pontuacoes_ordenadas.sort()
maior_pontuacao = pontuacoes_ordenadas[-1] # Maior pontuação entre os jogadores é o último item da lista de pontuações ordenadas

retorno = "" # Valor impresso no final do programa

if pontuacoes.count(maior_pontuacao) != 1: # Caso haja mais de um jogador com a maior pontuação
    retorno = "Rodada de cerveja para todos os jogadores!"
else:
    retorno = "O jogador número " + str(pontuacoes.index(maior_pontuacao)+1) + " vai receber o melhor bolo da cidade pois venceu com " + str(maior_pontuacao) + " ponto(s)!"

print(retorno)
