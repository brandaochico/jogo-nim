def computador_escolhe_jogada(n:int, m:int):
    jogada_do_computador : int = 0
    aux = 1
    i = 1

    frase_unica = "O Computador retirou uma peça do tabuleiro."

    if n - m == 0:
        jogada_do_computador = m
        if jogada_do_computador == 1:
            print(frase_unica)
        else:
            print("O computador retirou", jogada_do_computador, "peças.")
        return jogada_do_computador

    while aux <= m:
        while i <= 5:
            if n - aux == (m+1) * i:
                jogada_do_computador = aux
                if jogada_do_computador == 1:
                    print(frase_unica)
                else:
                    print("O computador retirou", jogada_do_computador, "peças.")
                return jogada_do_computador
            
            i += 1

        i = 0
        aux += 1

    jogada_do_computador = m
    if jogada_do_computador == 1:
        print(frase_unica)
    else:
        print("O computador retirou", jogada_do_computador, "peças.")
    return jogada_do_computador

def usuario_escolhe_jogada(n:int, m:int):
    jogada_do_usuario = int(input("Quantas peças você vai tirar? "))

    if jogada_do_usuario > m or jogada_do_usuario <= 0:
        print("Valor inválido!")
        return usuario_escolhe_jogada(n, m)

    return jogada_do_usuario

def partida():
    global vitorias_usuario
    global vitorias_computador

    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print()

    if m <= 0 or m >= n:
        print("Valores inválidos!")
        return partida()

    usuario_comeca : bool = False

    if (n % (m+1)) == 0:
        print("Você começa!")
        print()
        usuario_comeca = True
    else:
        print("Computador começa!")
        print()

    if usuario_comeca:
        while n >= 0:
            n = n - usuario_escolhe_jogada(n, m)
            if n <= 0:
                print("Você venceu!")
                vitorias_usuario += 1
                break
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                print("Agora restam", n, "peças no tabuleiro.")
            print()

            n = n - computador_escolhe_jogada(n, m)
            if n <= 0:
                print()
                print("Computador venceu!")
                vitorias_computador += 1
                break
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                print("Agora restam", n, "peças no tabuleiro.")
            print()
    
    else:
        while n >= 0:
            n = n - computador_escolhe_jogada(n, m)
            if n <= 0:
                print("Computador venceu!")
                vitorias_computador += 1
                break
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                print("Agora restam", n, "peças no tabuleiro.")
            print()

            n = n - usuario_escolhe_jogada(n, m)
            if n <= 0:
                print("Você venceu!")
                vitorias_usuario += 1
                break
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                print("Agora restam", n, "peças no tabuleiro.")
            print()


def campeonato():
    global vitorias_usuario
    global vitorias_computador

    print()
    print("**** Rodada 1 ****")
    print()
    partida()

    print()
    print("**** Rodada 2 ****")
    print()
    partida()

    print()
    print("**** Rodada 3 ****")
    print()
    partida()

    print()
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você", vitorias_usuario, "X", vitorias_computador, "Computador")

print("Bem-vindo ao jogo do NIM! Escolha:")
print()
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")

vitorias_usuario = 0
vitorias_computador = 0

escolha = int(input())

if escolha == 1:
    print("Você escolheu uma partida isolada!")
    partida()
else:
    print("Você escolheu um campeonato!")
    campeonato()

