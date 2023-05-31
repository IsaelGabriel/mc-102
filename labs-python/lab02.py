def create_question(query,extra_answers): # creates a custom yes or no question
    print(query)
    print("(0) Não")
    print("(1) Sim")
    for i in range(len(extra_answers)): # if there are extra possible answers, this makes the program print them
        print('(' + str(i + 2) + ') ' + extra_answers[i])
    answer = input()
    if not answer.isdigit(): # if the answer given is not a number, end program
        print("Opção inválida, recomece o questionário.")
        exit()
    if int(answer) >= 2 + len(extra_answers) or int(answer) < 0: # if the number given is higher than the number of options or lower than 0, end program
        print("Opção inválida, recomece o questionário.")
        exit()
    return int(answer)

first_answer = 0
last_answer = 0
distro_list = ""

print("Este é um sistema que irá te ajudar a escolher a sua próxima Distribuição Linux. Responda a algumas poucas perguntas para ter uma recomendação.")

match create_question("Seu SO anterior era Linux?",[]):
    case 0:
        first_answer = 0
        match create_question("Seu SO anterior era um MacOS?",[]):
            case 0:
                last_answer = 0
                distro_list = "Ubuntu Mate, Ubuntu Mint, Kubuntu, Manjaro"
            case 1:
                last_answer = 1
                distro_list = "ElementaryOS, ApricityOS"
    case 1:
        first_answer = 1
        match create_question("É programador/ desenvolvedor ou de áreas semelhantes?",["Sim, realizo testes e invasão de sistemas"]):
            case 0:
                last_answer = 0
                distro_list = "Ubuntu Mint, Fedora"
            case 1:
                last_answer = 1
                match create_question("Gostaria de algo pronto para uso ao invés de ficar configurando o SO?",[]):
                    case 0:
                        match create_question("Já utilizou Arch Linux?",[]):
                            case 0:
                                last_answer = 0
                                distro_list = "Antergos, Arch Linux"
                            case 1:
                                last_answer = 1
                                distro_list = "Gentoo, CentOS, Slackware"
                    case 1:
                        match create_question("Já utilizou Debian ou Ubuntu?",[]):
                            case 0:
                                last_answer = 0
                                distro_list = "OpenSuse, Ubuntu Mint, Ubuntu Mate, Ubuntu"
                            case 1:
                                last_answer = 1
                                distro_list = "Manjaro, ApricityOS"
            case 2:
                last_answer = 2
                distro_list = "Kali Linux, Black Arch"
                

path = ""
if first_answer == 1 and last_answer == 1:
    path = "Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições: "
elif first_answer == 0:
    path = "Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são: "
else:
    path = "Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: "

print(path + distro_list + ".")
