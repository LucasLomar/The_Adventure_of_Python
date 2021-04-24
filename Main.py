import os #INPORT DE COMANDOS DO SISTEMA OPERACIONAL (WINDOWS)

#AS CLASSES FICAM AQUI EM CIMA kkkkkkk

#PERSONAGEM
class Personagem:
    nivel=0
    hp=10
    mp=10
    arma=0
    armadura=0

#AS FUNCOES FICAM AQUI EMBAIXO KKKKKK

#FUNCAO EXIBE A TELA INICIAL DO JOGO
def telainicial():
    print("\nBEM VINDO\n")
    print("Escolha seu nome:\n")
    nome=input()
    os.system("cls")


#FUNCAO GERA UM NOVO PERSONAGEM (ATRIBUTOS INICIAIS)
def gerarpersonagem():
    Personagem.nivel=1
    print("Nivel: %i\n" %Personagem.nivel)

#FUNCAO EXIBE ELEMENTOS DO MAPA NA TELA
def mostrarmapa():
    print("\nLOCALIZAÇÃO: CIDADE CAPITAL\n")
    print(" 1 - TABERNA")
    print(" 2 - GUILDA")
    print(" 3 - ESTALAGEM")
    print(" 4 - LOJA")
    print(" 5 - CASTELO")
    print(" 6 - FLORESTA")
    print("\n")
    print("Tecle um numero para ir:\n")
    edificio=input()

#EXIBE O STATUS ATUAL DO PERSONAGEM
def verstatus():
    #print("Nome: %s" %Personagem.nome)
    print("Nivel: %i" %Personagem.nivel)
    print("HP: %i" %Personagem.hp)
    print("MP: %i" %Personagem.mp)
    print("Arma: %i" %Personagem.arma)
    print("Armadura: %i" %Personagem.armadura)

def novojogo():
    print("\nM - Exibir Mapa:      S - Exibir Statu:\n")
    acao=input()
    acao=acao.upper()
    os.system("cls")

    if acao == "M":
        mostrarmapa()
    if acao == "S":
        verstatus()


#Comandos do Jogo
telainicial()
gerarpersonagem()
novojogo()
