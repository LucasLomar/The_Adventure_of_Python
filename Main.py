import os
#Tela Inicial

def telainicial():
    print("\nBEM VINDO\n")
    print("Escolha seu nome:\n")
    nome=input()
    os.system("cls")

def gerarpersonagem():
    nivel=0
    hp=10
    mp=10
    arma=0
    armadura=0

def mostrarmapa():
    print("\nLOCALIZAÇÃO: CIDADE CAPITAL\n")
    print(" 1 - TABERNA")
    print(" 2 - GUILDA")
    print(" 3 - ESTALAGEM")
    print(" 4 - LOJA")
    print(" 5 - CASTELO")
    print(" 6 - FLORESTA")
    print("\n")
    prin("Tecle um numero para ir:\n")
    edificio=input()

def novojogo():
    mostrarmapa()



#Comandos do Jogo
telainicial()
#gerarpersonagem()
novojogo()
