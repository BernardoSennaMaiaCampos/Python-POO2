class Tabuleiro:
    def __init__(self, tamanho):
        self.tam=tamanho
    def print_tab(self):
        tab = [[1] * self.tam] * self.tam # define a matriz n x n
        traco = '+----' * self.tam # define o tamanho do traço
        print(traco + '+') # imprime linha superior
        for i in range(self.tam):
            for j in range (self.tam):
                print(f'| {tab[i][j]} ', end=" ") # "end = " " evita pular linha
            print('|')
            print(traco + '+') # imprime linha inferior
#Programa principal - objetos 
jogodavelha= Tabuleiro(3)
xadrez = Tabuleiro(8)
xadrez.print_tab()
jogodavelha.print_tab()