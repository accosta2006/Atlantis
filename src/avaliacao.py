import chess

valorPecas = {
    chess.PAWN: 100,
    chess.ROOK: 500,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.QUEEN: 900,
    chess.KING: 20000
}

avaliacaoPeaoBranco = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, 10, 10, 10, 10, 5,
    5, -5, -10, -10, -10, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0
]
avaliacaoPeaoPreto = list(reversed(avaliacaoPeaoBranco))

avaliacaoCavaloBranco = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 10, 10, 10, 10, 5, -30,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50
]

avaliacaoCavaloPreto = list(reversed(avaliacaoCavaloBranco))

avaliacaoBispoBranco = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20
]
avaliacaoBispoPreto = list(reversed(avaliacaoBispoBranco))

avaliacaoTorreBranca = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0
]
avaliacaoTorrePreto = list(reversed(avaliacaoTorreBranca))

avaliacaoDamaBranca = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -5, 0, 5, 5, 5, 5, 0, -5,
    0, 0, 5, 5, 5, 5, 0, -5,
    -10, 5, 5, 5, 5, 5, 0, -10,
    -10, 0, 5, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20
]

avaliacaoDamaPreta = list(reversed(avaliacaoDamaBranca))

avaliacaoReiBranco = [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30
]
avaliacaoReiPreto = list(reversed(avaliacaoReiBranco))

avaliacaoReiFinalBranco = [
    50, -30, -30, -30, -30, -30, -30, -50,
    -30, -30,  0,  0,  0,  0, -30, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 20, 30, 
]

avaliacaoReiFinalPreto = list(reversed(avaliacaoReiFinalBranco))

def avaliarPeca(peca, sqr, final):
    tipo_peca = peca.piece_type
    mapeamento = []

    if 0 <= sqr < len(mapeamento):
        return mapeamento[sqr]
    else:
        return 0

    if tipo_peca == chess.PAWN:
        if peca.color == chess.WHITE:    
            mapeamento = avaliacaoPeaoBranco
        
        else:
            mapeamento = avaliacaoPeaoPreto
        
    if tipo_peca == chess.KNIGHT:
        if peca.color == chess.WHITE:
            mapeamento == avaliacaoCavaloBranco
        
        else:
            mapeamento == avaliacaoCavaloPreto
    
    if tipo_peca == chess.BISHOP:
        if peca.color == chess.WHITE:
            mapeamento == avaliacaoBispoBranco
        
        else:
            mapeamento = avaliacaoBispoPreto
    
    if tipo_peca == chess.ROOK:
        if peca.color == chess.WHITE:
            mapeamento = avaliacaoTorreBranca
        
        else:
            mapeamento = avaliacaoTorrePreto
    
    if tipo_peca == chess.QUEEN:
        if peca.color == chess.WHITE:
            mapeamento = avaliacaoDamaBranca
        
        else:
            mapeamento = avaliacaoDamaPreta
    
    if tipo_peca == chess.KING and final == False:
        if peca.color == chess.WHITE:
            mapeamento = avaliacaoReiBranco
        
        else:
            mapeamento = avaliacaoReiPreto

    if tipo_peca == chess.KING and final == True:
        if peca.color == chess.WHITE:
            mapeamento = avaliacaoReiFinalBranco
        
        else:
            mapeamento = avaliacaoReiFinalPreto
    
    return mapeamento[sqr]

def valorJogada(board, jog, final):
    if jog.promotion is not None:
        if board.turn == chess.BLACK:
            return -float("inf")
        
        else:
            float("inf")

    peca = board.piece_at(jog.from_square)

    if peca:
        de = avaliarPeca(peca, jog.from_square, final)
        para = avaliarPeca(peca, jog.to_square, final)
        valor_pos = para - de
    
    else:
        raise Exception(f"É necessário uma peça em {jog.from_square}")
    
    valor_captura = 0
    if board.is_capture(jog):
        valor_captura = avaliacaoCaptura(board, jog)
    
    valor_atual = valor_captura + valor_pos

    if board.turn == chess.BLACK:
        valor_atual = -valor_atual
    
    return valor_atual

def avaliarTabuleiro(board):
    pont = 0
    final = verificarFinal(board)

    for sqr in chess.SQUARES:
        peca = board.piece_at(sqr)
        if not peca:
            continue

        else:
            peca = board.piece_at(sqr)
            pont += valorPecas[peca.piece_type] + avaliarPeca(peca, sqr, final)
    
    return pont

def verificarFinal(board):
    damas = 0
    cavBis = 0

    for sqr in chess.SQUARES:
        peca = board.piece_at(sqr)
        if peca and peca.piece_type == chess.QUEEN:
            damas += 1
        
        if peca and (peca.piece_type == chess.BISHOP or peca.piece_type == chess.KNIGHT):
            cavBis += 1

    if damas == 0 or (damas == 2 and cavBis <= 1):
        return True

    return False

def avaliacaoCaptura(board, jog):

    if board.is_en_passant(jog):
        return valorPecas[chess.PAWN]
    
    para = board.piece_at(jog.to_square)
    de = board.piece_at(jog.from_square)

    if para is None or de is None:
        raise Exception(f"São necessárias peças nos quadrados {jog.to_square} e {jog.from_square}")
    
    return valorPecas[para.piece_type] - valorPecas[de.piece_type]

