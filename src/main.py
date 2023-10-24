import chess
import gerador

cor = input("Escolha a sua cor (b/p):\n")
prof = int(input("Escolha a profundidade:\n"))
game = chess.Board()

def jogadaEngine(board, prof):
    jogada_cpu = gerador.proxJog(prof, board)
    board.push(jogada_cpu)
    print("O engine jogou: " + str(jogada_cpu))

def jogadaJogador(board):
    jogada = input("A tua jogada (ex.: e4, Nf3)")
    board.push_san(jogada)

while not game.is_checkmate():
    if cor == 'p':
        jogadaEngine(game, prof)
        jogadaJogador(game)
    
    if cor == 'b':
        jogadaJogador(game)
        jogadaEngine(game, prof)