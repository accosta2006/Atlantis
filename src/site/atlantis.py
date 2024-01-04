import chess
import random

class Engine:
    def __init__(self, tab, profmax, cor):
        self.tab = tab
        self.cor = cor
        self.profmax = profmax

    def melhorJogada(self):
        return self.minimax(None, 1)

    def valorPecas(self, quad):
        valorPeca = 0

        if self.tab.piece_type_at(quad) == chess.PAWN:
            valorPeca = 1
        
        elif self.tab.piece_type_at(quad) == chess.KNIGHT:
            valorPeca = 3.2

        elif self.tab.piece_type_at(quad) == chess.BISHOP:
            valorPeca = 3.33
        
        elif self.tab.piece_type_at(quad) == chess.ROOK:
            valorPeca = 5.1
        
        elif self.tab.piece_type_at(quad) == chess.QUEEN:
            valorPeca = 8.8
        
        if self.tab.color_at(quad) != self.cor:
            return -valorPeca
        
        else:
            return valorPeca

    def avalTab(self):
        valor = 0

        for i in range(64):
            valor += self.valorPecas(chess.SQUARES[i])
        valor += self.mate() + self.abertura() + 0.001 * random.random()
        
        return valor
    
    def mate(self):
        if self.tab.is_checkmate():
            if self.tab.turn == chess.WHITE:
                return -9999
            else:
                return 9999
        else:
            return 0
    
    def abertura(self):
        if self.tab.fullmove_number <= 10:
            if self.tab.turn == chess.WHITE:
                return 1/30 * self.tab.legal_moves.count()
            else:
                return 1/30 * self.tab.legal_moves.count()
        else:
            return 0
            
    def minimax(self, cand, prof):
        if ( prof == self.profmax or self.tab.legal_moves.count() == 0):
            return self.avalTab()
        
        else:
            jogadas = list(self.tab.legal_moves)

            novoCand = None

            if(prof % 2 != 0):
                novoCand = float("-inf")
            else:
                novoCand = float("inf")
            
            for i in jogadas:

                self.tab.push(i)
                valor = self.minimax(novoCand, prof + 1) 

                if(valor > novoCand and prof % 2 != 0):
                    if (prof == 1):
                        jog=i
                    novoCand = valor

                elif(valor < novoCand and prof % 2 == 0):
                    novoCand = valor

                if (cand != None
                 and valor < cand
                 and prof % 2 == 0):
                    self.tab.pop()
                    break

                elif (cand != None 
                and valor > cand 
                and prof % 2 != 0):
                    self.tab.pop()
                    break

                self.tab.pop()

            if (prof>1):
                return novoCand
            else:
                return jog

def generateMove(fen, profmax, cor):
    tab = chess.Board(fen)
    engine = Engine(tab, profmax, cor)
    jog = engine.melhorJogada()

    return jog