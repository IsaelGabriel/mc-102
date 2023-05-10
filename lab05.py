def reverter(genoma : str, parametros : list[str]) -> str:
    i = int(parametros[0])
    j = int(parametros[1]) + 1
    if i >= len(genoma)-1: return genoma
    if j > len(genoma): j = len(genoma)

    return genoma[0:i] + genoma[i:j][::-1] + genoma[j:]
    

def transpor(genoma : str, parametros : list[str]) -> str:
    i = int(parametros[0])
    j = int(parametros[1]) + 1
    k = int(parametros[2]) + 1

    if i >= len(genoma)-1: return genoma
    if j > len(genoma)-1: return genoma

    return genoma[0:i] + genoma[j:k] + genoma[i:j] + genoma[k:]
    

def combinar(genoma : str, parametros : list[str]) -> str:
    g = parametros[0]
    i = int(parametros[1])

    return genoma[0:i] + g + genoma[i:]

def concatenar(genoma : str, parametros : list[str]) -> str:
    return genoma + parametros[0]

def remover(genoma : str, parametros : list[str]) -> str:
    i = int(parametros[0])
    j = int(parametros[1]) + 1
    if i > j-1: return genoma
    return genoma[:i] + genoma[j:]

def transpor_e_reverter(genoma : str, parametros : list[str]) -> int:
    genoma = transpor(genoma, parametros)
    return reverter(genoma, [parametros[0],parametros[2]])

def buscar(genoma : str, parametro : list[str]) -> str:
    genoma_copia = genoma
    alvo = parametro
    contagem = 0
    while alvo in genoma_copia:
        contagem += 1
        indice = genoma_copia.index(alvo)
        genoma_copia = genoma_copia[:indice] + genoma_copia[(indice + len(alvo)):]
    return contagem


def buscar_bidirecional(genoma : str, parametro : list[str]) -> int:
    return buscar(genoma, parametro) + buscar(genoma[::-1], parametro)
    

def main():
    genoma_referecia = input()
    saida = "" # escrito na tela no ao final da execução
    linha = "" # comando digitado pelo usuário
    comandos = {
        "reverter": reverter,
        "transpor": transpor,
        "combinar": combinar,
        "concatenar": concatenar,
        "remover" : remover,
        "transpor_e_reverter": transpor_e_reverter
    } # cada chave remete a uma função

    while linha != "sair":
        linha = input()
        if linha != "sair":
            if linha == "mostrar": saida += genoma_referecia + "\n"
            elif "buscar" in linha:
                if linha.split()[0] == "buscar": saida += str(buscar(genoma_referecia,linha.split()[1])) + "\n"
                else: saida += str(buscar_bidirecional(genoma_referecia,linha.split()[1])) + "\n"
            else: genoma_referecia = comandos[linha.split()[0]](genoma_referecia,linha.split()[1:])
    print(saida)

if __name__ == "__main__": main()