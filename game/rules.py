# from game.pieces import get_piece_type


def is_valid_move(board, sr, sc, er, ec):

    piece = board[sr][sc]
    piece_type = get_piece_type(piece)

    if piece_type == "pawn":
        return valid_pawn_move(board, sr, sc, er, ec)

    elif piece_type == "rook":
        return valid_rook_move(board, sr, sc, er, ec)

    elif piece_type == "knight":
        return valid_knight_move(board, sr, sc, er, ec)

    elif piece_type == "bishop":
        return valid_bishop_move(board, sr, sc, er, ec)

    elif piece_type == "queen":
        return valid_queen_move(board, sr, sc, er, ec)

    elif piece_type == "king":
        return valid_king_move(board, sr, sc, er, ec)

    return False


def valid_pawn_move(board, sr, sc, er, ec):

    # 前進一格
    if sc == ec and er == sr - 1 and board[er][ec] == " ":
        return True

    # 第一歩兩格
    if sr == 6 and sc == ec and er == sr - 2:
        if board[sr - 1][sc] == " " and board[er][ec] == " ":
            return True

    # 斜吃
    if er == sr - 1 and abs(ec - sc) == 1:
        if board[er][ec] != " ":
            return True

    return False

def valid_rook_move(board, sr, sc, er, ec):

    #非直線移動
    if sr != er and sc != ec:
        return False

    # 水平移動
    if sr == er:
        step = 1 if ec > sc else -1
        for c in range(sc + step, ec, step):
            if board[sr][c] != " ":
                return False

    # 垂直移動
    if sc == ec:
        step = 1 if er > sr else -1
        for r in range(sr + step, er, step):
            if board[r][sc] != " ":
                return False

    return True
    
 




    return False




# pawn ✔
# rook 1
# knight
# bishop
# queen
# king

# def path_clear(board, sr, sc, er, ec)

# rook / bishop / queen 全部共用。