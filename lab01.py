jog_sheila = input() # Jogada da Sheila.
jog_reginaldo = input() # Jogada do Reginaldo.

# Regras do jogo em um dict, cada chave contém o indice da jogada que derrota.
jogo = {
    "pedra" : [2,3],
    "papel" : [0,4],
    "tesoura" : [1,3],
    "lagarto" : [4,1],
    "spock" : [2,0]
    }

derrotaveis_reginaldo = [list(jogo.keys())[i] for i in jogo[jog_reginaldo]] # Lista dos nomes das jogadas derrotaveis por Reginaldo.
derrotaveis_sheila = [list(jogo.keys())[i] for i in jogo[jog_sheila]] # Lista dos nomes das jogadas derrotaveis por Sheila.

resultado = "empate" # Valor a ser imprimido pelo programa. Caso nenhum dos jogadores vença, valor permanece inalterado.

if(jog_sheila in derrotaveis_reginaldo): # Se a jogada de Sheila for derrotavel por Reginaldo...
    resultado = "Jornada nas Estrelas"
elif(jog_reginaldo in derrotaveis_sheila): # Se a jogada de Reginaldo for derrotavel por Sheila...
    resultado = "Interestelar"

print(resultado) #Imprima o valor de resultado
