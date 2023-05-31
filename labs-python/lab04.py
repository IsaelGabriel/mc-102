dias = int(input()) # quantidade de dias a serem analisados

texto_saida = "" # texto de retorno do programa

for dia in range(dias): # repete a cada dia analisado
    qtd_pares_brigas = int(input()) # quantidade de pares de animasi que brigam entre si
    pares_brigas = {} # dicionario de animais que brigam entre si, sendo a chave o nome de um animal e o resultado a lista dos animais com que briga
    for i in range(qtd_pares_brigas):
        pets = input().split()
        for j in range(2):
            if(pets[0] not in pares_brigas.keys()):
                pares_brigas[pets[0]] = [pets[1]]
            else:
                pares_brigas[pets[0]].append(pets[1])
            pets = pets[::-1] # inverter a lista e repetir o processo para listar as brigas de ambos os animais

    lista_procedimentos = input().split()
    procedimentos_disponiveis = {} # dicionario de procedimentos disponiveis do dia, sendo a chave o nome do procedimento e o resultado a quantidade
    for i in range(0,len(lista_procedimentos),2):
        procedimentos_disponiveis[lista_procedimentos[i]] = int(lista_procedimentos[i+1])

    qtd_pets_dia = int(input()) # numero de pets que vieram ao petshop no dia
    pets_dia = [] # Lista de pets que foram ao petshop no dia (por ordem de chegada)
    pets_atendidos = [] # Lista de pets que foram atendidos no dia
    pets_nao_atendidos = [] # Lista de pets que nao foram atendidos no dia por falta de quantidade no procedimento solicitado
    procedimentos_indisponiveis = [] # Lista de pets que nao foram atendidos no dia pois o procedimento solicidado nao estava disponivel no dia

    # Checagem de procedimentos
    for i in range(qtd_pets_dia): 
        procedimento = input().split() # Linha que contem procedimento solicitado no formato [pet, procedimento]
        pets_dia.append(procedimento[0])
        
        if procedimento[1] not in procedimentos_disponiveis.keys(): # Caso procedimento não disponível no dia
            procedimentos_indisponiveis.append(procedimento[0])
            continue
        
        if(procedimentos_disponiveis[procedimento[1]] > 0): # Caso procedimento ainda possa ser realizado
            procedimentos_disponiveis[procedimento[1]] -= 1
            pets_atendidos.append(procedimento[0])
        else: # Caso procedimento não possa mais ser realizado
            pets_nao_atendidos.append(procedimento[0])
    
    # Checagem de brigas
    brigas_dia = [] # Pares de pets que brigaram no dia
    for pet_a in pets_dia:
        if(pet_a in pares_brigas.keys()): # Se o pet_a se envolve em brigas
            for pet_b in pares_brigas[pet_a]: # Para cada pet que o pet_a briga
                if pet_b in pets_dia: # Se o pet_b está no petshop no dia
                    par = [pet_a,pet_b]
                    if (par not in brigas_dia) and (par[::-1] not in brigas_dia): # Caso o par não esteja ainda na lista de brigas_dia
                        brigas_dia.append(par)
    
    # Adicionar ao texto de saida
    texto_saida += "Dia: " + str(dia+1) + "\n"
    texto_saida += "Brigas: " + str(len(brigas_dia)) + "\n"

    # Texto de animais atendidos
    if len(pets_atendidos) >= 1:
        texto_saida += "Animais atendidos: "
        for pet in pets_atendidos:
            texto_saida += pet + ", "
        texto_saida = texto_saida[:-2] + "\n"
    
    # Texto de animais não atendidos
    if len(pets_nao_atendidos) >= 1:
        texto_saida += "Animais não atendidos: "
        for pet in pets_nao_atendidos:
            texto_saida += pet + ", "
        texto_saida = texto_saida[:-2] + "\n"
    
    # Texto de procedimentos indisponíveis
    if len(procedimentos_indisponiveis) >= 1:
        for pet in procedimentos_indisponiveis:
            texto_saida += "Animal " + pet + " solicitou procedimento não disponível.\n"
    if dia+1 < dias: texto_saida += "\n" # Caso não seja o ultimo dia, pular mais uma linha

print(texto_saida)