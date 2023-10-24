import chess
from avaliacao import avaliarTabuleiro, valorJogada, verificarFinal

PONT_MATE = 10000000000
LIMI_MATE =  9990000000

def proxJog(prof, board):
    jog = minimax_main(prof, board)

    return jog

def ordenarJogadas(board):
    final = verificarFinal(board)

    def ordenar(jog):
        return valorJogada(board, jog, final)
    
    ordem = sorted(
        board.legal_moves, key=ordenar, reverse=(board.turn == chess.WHITE)
    )
    return list(ordem)

def minimax_main(prof, board: chess.Board()):
    maximizar = chess.WHITE
    melhorJog = -float("inf")
    if not maximizar:
        melhorJog = float("inf")
    
    jogadas = ordenarJogadas(board)
    primJogada = jogadas[0]

    for jog in jogadas:
        board.push(jog)

        if board.can_claim_draw():
            valor = 0.0
        
        else:
            valor = minimax(prof - 1, board, -float("inf"), float("inf"), not maximizar)

        board.pop()
        if maximizar and valor >= melhorJog:
            melhorJog = valor
            primJogada = jog

        elif not maximizar and valor <= melhorJog:
            melhorJog = valor
            primJogada = jog

    return primJogada

def minimax(prof, board, alpha, beta, maximizar):
    if board.is_checkmate():
        if maximizar:
            return -PONT_MATE  

        else:
            return PONT_MATE

    elif board.is_game_over():
        return 0

    if prof == 0:
        return avaliarTabuleiro(board)

    if maximizar:
        melhorJog = -float("inf")
        jogadas = ordenarJogadas(board)
        for jog in jogadas:
            board.push(jog)
            jog_atual = minimax(prof - 1, board, alpha, beta, not maximizar)

            if jog_atual > LIMI_MATE:
                jog_atual -= 1
            
            elif jog_atual < -LIMI_MATE:
                jog_atual += 1
            
            melhorJog = max(melhorJog, jog_atual)
            board.pop()
            alpha = max(alpha, melhorJog)
            if beta <= alpha:
                return melhorJog
        
        return melhorJog
    else:
        melhorJog = float("inf")
        jogadas = ordenarJogadas(board)
        for jog in jogadas:
            board.push(jog)
            jog_atual = minimax(prof - 1, board, alpha, beta, not maximizar)

            if jog_atual > LIMI_MATE:
                jog_atual -= 1
            
            elif jog_atual < -LIMI_MATE:
                jog_atual += 1
            
            melhorJog = min(melhorJog, jog_atual)
            board.pop()
            alpha = min(alpha, melhorJog)
            if beta <= alpha:
                return melhorJog
        
        return melhorJog