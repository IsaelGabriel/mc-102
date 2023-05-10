def encontrar_ind(mensagem: list[str], alvo: str, ind_minimo: int = 0) -> int:
    # mensagem transferida de list para string
    string_mensagem = "".join(mensagem)
    for i in range(ind_minimo, len(string_mensagem)):
        if len(alvo) == 1:
            if string_mensagem[i] == alvo:
                return i
        elif alvo == "numero":
            indice_char = ord(string_mensagem[i])
            if indice_char >= 48 and indice_char <= 57:
                return i
        elif alvo == "vogal":
            if string_mensagem[i] in "AEIOUaeiou":
                return i
        elif alvo == "consoante":
            indice_char = ord(string_mensagem[i])
            letra_maiuscula = (indice_char >= 65 and indice_char <= 90)
            letra_minuscula = (indice_char >= 97 and indice_char <= 122)
            letra = letra_maiuscula or letra_minuscula
            if letra and string_mensagem[i] not in "AEIOUaeiou":
                return i
    return 0


def encontrar_chave(operacao: str, n_1: int, n_2: int) -> int:
    if operacao == "+":
        return n_1 + n_2
    elif operacao == "-":
        return n_1 - n_2
    else:
        return n_1 * n_2


def decodificar_caractere(char: str, chave: int) -> str:
    indice_char = int(ord(char) + chave) - 32

    if indice_char > 94:
        indice_char = indice_char % 95
    if indice_char < 0:
        indice_char += 95

    # retornar o caractere correspondente ao novo indice_char
    return chr(indice_char + 32)


def main() -> None:
    # tipo da operação a ser utilizada ["+","-" ou "*"]
    operacao = input()
    # caractere ou tipo de caractere a ser procurado
    alvo_1 = input()
    # caractere ou tipo de caractere a ser procurado
    alvo_2 = input()
    # numero de linhas da mensagem
    q_linhas = int(input())
    # mensagem em q_linhas
    mensagem = [input() for n in range(q_linhas)]

    # indice do alvo_1 na mensagem (primeira ocorrencia)
    ind_alvo_1 = encontrar_ind(mensagem, alvo_1)
    # indice do alvo_2 na mensagem (primeira ocorrencia após ind_alvo_1)
    ind_alvo_2 = encontrar_ind(mensagem, alvo_2, ind_alvo_1)

    # chave de criptografia
    chave = encontrar_chave(operacao, ind_alvo_1, ind_alvo_2)

    print(chave)

    # para cada linha da mensagem
    for linha in mensagem:
        linha_decodificada = ""
        for char in linha:
            # decodificar caractere
            linha_decodificada += decodificar_caractere(char, chave)
        # exibir linha
        print(linha_decodificada)


if __name__ == "__main__":
    main()
