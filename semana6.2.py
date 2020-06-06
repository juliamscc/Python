def jogo_do_nim():
    print("Bem vindo ao jogo do NIM! Escolha:")
    print(" ")
    print("1- para jogar uma partida")
    tipo_de_jogo = int(input("2- para jogar um campeonato "))
    comp_ganhou = False
    while tipo_de_jogo != 1 and tipo_de_jogo != 2:
        tipo_de_jogo = int(input("Por favor, escolha 1 ou 2. "))
    if tipo_de_jogo == 1:
        print("Você escolheu uma partida!")
        print(" ")
        comp_ganhou = partida()
        if comp_ganhou:
            print("Fim de jogo! O computador ganhou!")
        else:
            print("Fim de jogo! Você ganhou!")
    else: 
        print("Você escolheu um campeonato!")
        print(" ")
        x = 1
        pontosU = 0
        pontosC = 0
        while x <= 3:
            print("***** Rodada",x,"*****")
            print(" ")
            comp_ganhou = partida ()
            if comp_ganhou:
                pontosC = pontosC + 1
            else:
                pontosU = pontosU + 1
            x = x + 1
        print("Fim do campeonato!")
        print("Placar: Você",pontosU,"X",pontosC,"Computador")

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Qual o limite de peças por jogada? "))
    print(" ")
    while n <= 0 or m <= 0 or n <= m:
        print("Por favor, insira quantidades válidas")
        n = int(input("Quantas peças? "))
        m = int(input("Qual o limite de peças por jogada? "))
        print(" ")
    qtde_pecas_rest = n
    comp_comecou = False
    if n % (m + 1) == 0:
        print("Computador começa!")
        print(" ")
        jogada = computador_escolhe_jogada(n,m)
        qtde_pecas_rest = qtde_pecas_rest - jogada
        print("O computador tirou",jogada,"peça(s).")
        print("Agora restam",qtde_pecas_rest,"peça(s).")
        print(" ")
        comp_comecou = True
    else:
        print("Você começa!")
        print(" ")
        jogada = usuario_escolhe_jogada(n,m)
        qtde_pecas_rest = qtde_pecas_rest - jogada
        print("Você tirou",jogada,"peça(s).")
        print("Agora restam",qtde_pecas_rest,"peça(s).")
        print(" ")
        comp_comecou = False 
    while qtde_pecas_rest > 0:
        if comp_comecou:
            jogada = usuario_escolhe_jogada(qtde_pecas_rest,m)
            qtde_pecas_rest = qtde_pecas_rest - jogada
            print("Você tirou",jogada,"peça(s).")
            print("Agora restam",qtde_pecas_rest,"peça(s).")
            print(" ")
            if qtde_pecas_rest == 0:
                return False
                break
            jogada = computador_escolhe_jogada(qtde_pecas_rest,m)
            qtde_pecas_rest = qtde_pecas_rest - jogada
            print("O computador tirou",jogada,"peça(s).")
            print("Agora restam",qtde_pecas_rest,"peça(s).")
            print(" ")
            if qtde_pecas_rest == 0:
                return True
        else:
            jogada = computador_escolhe_jogada(qtde_pecas_rest,m)
            qtde_pecas_rest = qtde_pecas_rest - jogada
            print("O computador tirou",jogada,"peça(s).")
            print("Agora restam",qtde_pecas_rest,"peça(s).")
            print(" ")
            if qtde_pecas_rest == 0:
                return True
                break
            jogada = usuario_escolhe_jogada(qtde_pecas_rest,m)
            qtde_pecas_rest = qtde_pecas_rest - jogada
            print("Você tirou",jogada,"peça(s).")
            print("Agora restam",qtde_pecas_rest,"peça(s).")
            print(" ")
            if qtde_pecas_rest == 0:
                return False

def computador_escolhe_jogada(n,m):
    jogada = 1
    while jogada <= m:
        if (n - jogada) % (m + 1) == 0:
            return jogada
        else:
            jogada = jogada + 1
            if jogada == m:
                return m
    
def usuario_escolhe_jogada(n,m):
    jogada = int(input("Quantas peças você vai tirar? "))
    while not (jogada > 0) or not (jogada <= m):
        print ("Oops! Jogada inválida! Tende de novo.")
        print(" ")
        jogada = int(input("Quantas peças você vai tirar? "))
    return jogada

jogo_do_nim()
    
