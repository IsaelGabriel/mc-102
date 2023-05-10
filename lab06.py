def preencher_vetores(vetor1: list[int], vetor2: list[int], n: int) -> None:
    if len(vetor1) < len(vetor2):
        vetor1 += [n] * (len(vetor2)-len(vetor1))
    if len(vetor2) < len(vetor1):
        vetor2 += [n] * (len(vetor1) - len(vetor2))


def soma_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    vetor_resultante: list[int] = []

    preencher_vetores(vetor1, vetor2, 0)

    for i in range(len(vetor1)):
        vetor_resultante.append(vetor1[i]+vetor2[i])

    return vetor_resultante


def subtrai_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    vetor_resultante: list[int] = []

    preencher_vetores(vetor1, vetor2, 0)

    for i in range(len(vetor1)):
        vetor_resultante.append(vetor1[i]-vetor2[i])

    return vetor_resultante


def multiplica_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    vetor_resultante: list[int] = []

    preencher_vetores(vetor1, vetor2, 1)

    for i in range(len(vetor1)):
        vetor_resultante.append(vetor1[i]*vetor2[i])

    return vetor_resultante


def divide_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    vetor_resultante: list[int] = []

    if len(vetor1) < len(vetor2):
        vetor1 += [0] * (len(vetor2)-len(vetor1))
    elif len(vetor2) < len(vetor1):
        vetor2 += [1] * (len(vetor1) - len(vetor2))

    for i in range(len(vetor1)):
        vetor_resultante.append(vetor1[i]//vetor2[i])

    return vetor_resultante


def multiplicacao_escalar(vetor: list[int], escalar: int) -> list[int]:
    for i in range(len(vetor)):
        vetor[i] *= escalar

    return vetor


def n_duplicacao(vetor: list[int], n: int) -> list[int]:
    vetor *= n
    return vetor


def soma_elementos(vetor: list[int]) -> int:
    soma = 0
    for valor in vetor:
        soma += valor

    return soma


def produto_interno(vetor1: list[int], vetor2: list[int]) -> int:
    produto = 0

    preencher_vetores(vetor1, vetor2, 1)

    for i in range(len(vetor1)):
        produto += vetor1[i]*vetor2[i]

    return produto


def multiplica_todos(vetor1: list[int], vetor2: list[int]) -> list[int]:
    for i in range(len(vetor1)):
        valor = 0
        for j in vetor2:
            valor += vetor1[i] * j

        vetor1[i] = valor

    return vetor1


def correlacao_cruzada(vetor: list[int], mascara: list[int]) -> list[int]:
    vetor_resultante: list[int] = []
    k = len(mascara)
    n = len(vetor)

    for i in range(n - k + 1):
        valor = 0
        for j in range(k):
            valor += vetor[i+j]*mascara[j]
        vetor_resultante.append(valor)

    return vetor_resultante


def main() -> None:
    vetor_atual = [int(x) for x in input().split(",")]
    retorno = ""

    comandos = {
        "soma_vetores": soma_vetores,
        "subtrai_vetores": subtrai_vetores,
        "multiplica_vetores":  multiplica_vetores,
        "divide_vetores": divide_vetores,
        "multiplicacao_escalar": multiplicacao_escalar,
        "n_duplicacao": n_duplicacao,
        "produto_interno": produto_interno,
        "multiplica_todos": multiplica_todos,
        "correlacao_cruzada": correlacao_cruzada
    }

    comando_atual = input()
    while comando_atual != "fim":
        if comando_atual == "soma_elementos":
            vetor_atual = [soma_elementos(vetor_atual)]
        elif comando_atual in ["multiplicacao_escalar", "n_duplicacao"]:
            vetor_atual = comandos[comando_atual](vetor_atual, int(input()))
        else:
            vetor2 = [int(x) for x in input().split(",")]
            retorno_comando = comandos[comando_atual](vetor_atual, vetor2)

            if comando_atual == "produto_interno":
                vetor_atual = [retorno_comando]
            else:
                vetor_atual = retorno_comando

        retorno += str(vetor_atual) + "\n"

        comando_atual = input()

    print(retorno)


if __name__ == "__main__":
    main()
