def main():
    filmes = [input() for i in range(int(input()))]
    n_avaliacoes = int(input())
    avaliacoes = {}
    for filme in filmes:
        avaliacoes[filme] = {
            "filme que causou mais bocejos": [],
            "filme que foi mais pausado": [],
            "filme que mais revirou olhos": [],
            "filme que não gerou discussão nas redes sociais": [],
            "enredo mais sem noção": [],
            "avaliado": False
        }
    categorias: list[str]
    for i in range(n_avaliacoes):
        avaliacao = input().split(", ")[1:]
        avaliacoes[avaliacao[1]][avaliacao[0]].append(int(avaliacao[2]))
        avaliacoes[avaliacao[1]]["avaliado"] = True
    
    categorias_simples = {
        "filme que causou mais bocejos": "",
        "filme que foi mais pausado": "",
        "filme que mais revirou olhos": "",
        "filme que não gerou discussão nas redes sociais": "",
        "enredo mais sem noção": "",
    }
    
    categorias_especiais = {
        "pior filme do ano": [],
        "não merecia estar aqui": []
    }

    for categoria in categorias_simples.keys():
        maior_media = 0.0
        filmes_vencedores = []

        for filme in filmes:
            if len(avaliacoes[filme][categoria]) > 0:
                media_atual = sum(avaliacoes[filme][categoria]) / len(avaliacoes[filme][categoria])
                if media_atual > maior_media:
                    maior_media = media_atual
                    filmes_vencedores = [filme]
                elif media_atual == maior_media:
                    filmes_vencedores.append(filme)

        if len(filmes_vencedores) > 1:
            mais_avaliacoes = filmes_vencedores[0]
            for filme in filmes_vencedores:
                if len(avaliacoes[filme][categoria]) > len(avaliacoes[mais_avaliacoes][categoria]):
                    mais_avaliacoes = filme
            categorias_simples[categoria] = mais_avaliacoes
        else:
            categorias_simples[categoria] = filmes_vencedores[0]

    filmes_ganhadores_simples = set(categorias_simples.values())

    categorias_especiais["pior filme do ano"] = [list(filmes_ganhadores_simples)[0]]

    for filme in filmes_ganhadores_simples:
        if list(categorias_simples.values()).count(filme) > list(categorias_simples.values()).count(categorias_especiais["pior filme do ano"][0]):
            categorias_especiais["pior filme do ano"] = [filme]
        elif list(categorias_simples.values()).count(filme) == list(categorias_simples.values()).count(categorias_especiais["pior filme do ano"][0]):
            categorias_especiais["pior filme do ano"].append(filme)
    
    if len(categorias_especiais["pior filme do ano"]) == 1:
        categorias_especiais["pior filme do ano"] = categorias_especiais["pior filme do ano"][0]
    else:
        maior_soma = 0.0
        filme_vencedor = ""
        for filme in categorias_especiais["pior filme do ano"]:
            soma_atual = 0.0
            for categoria in categorias_simples.keys():
                if len(avaliacoes[filme][categoria]) >= 1:
                    soma_atual += sum(avaliacoes[filme][categoria])/len(avaliacoes[filme][categoria])
            if soma_atual > maior_soma:
                filme_vencedor = filme
                maior_soma = soma_atual

    for filme in filmes:
        if not avaliacoes[filme]["avaliado"]: 
            categorias_especiais["não merecia estar aqui"].append(filme)

    print("#### abacaxi de ouro ####\n")
    
    print("categorias simples")
    
    for categoria, filme in categorias_simples.items():
        print(f"categoria: {categoria}")
        print(f"- {filme}")
    
    print("\ncategorias especiais")

    print("prêmio pior filme do ano")

    print(f"- {categorias_especiais['pior filme do ano']}")

    print("prêmio não merecia estar aqui")
    if len(categorias_especiais["não merecia estar aqui"]) < 1:
        print("- sem ganhadores")
    else:
        print(f"- {', '.join(categorias_especiais['não merecia estar aqui'])}")



if __name__ == "__main__":
    main()