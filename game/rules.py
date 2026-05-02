from game.pieces import get_piece_type


def is_valid_move(board, sr, sc, er, ec):
    #取得棋子類別
    piece = board[sr][sc]
    piece_type = get_piece_type(piece)

    #依據棋子類別檢驗相應規則
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
    piece = board[sr][sc]
    
    if piece.isupper(): # 黑棋
        direction = 1   # 作為檢查棋子移動用的方向, 以左上角為座標 (0, 0)
        start_row = 1
    else:               # 白棋
        direction = -1
        start_row = 6


    # 1. 前進一格 (+ direction)
    if sc == ec and er == sr + direction and board[er][ec] == " ":
        return True

    # 2. 第一步可走兩格
    if sr == start_row and sc == ec and er == sr + 2 * direction:
        # 檢查中間那格
        if board[sr + direction][sc] == " " and board[er][ec] == " ":
            return True
 
    # 3. 斜吃
    if er == sr + direction and abs(ec - sc) == 1:
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
    


def valid_bishop_move(board, sr, sc, er, ec):

    #非斜線移動
    if abs(er - sr) != abs(ec - sc):
        return False

    # 斜線移動
    if abs(er - sr) == abs(ec - sc):
        step_ver = 1 if ec > sc else -1
        step_hoi = 1 if er > sr else -1

        curr_r = sr + step_hoi
        curr_c = sc + step_ver
        while curr_r != er: # 因為是斜角，檢查完 r, c 也到了
            if board[curr_r][curr_c] != " ":
                return False
            curr_r += step_hoi
            curr_c += step_ver

    return True


def valid_queen_move(board, sr, sc, er, ec):

    #非斜線移動
    if abs(er - sr) != abs(ec - sc) and sr != er and sc != ec:
        return False
    
    # 斜線移動
    if abs(er - sr) == abs(ec - sc):
        step_ver = 1 if ec > sc else -1
        step_hoi = 1 if er > sr else -1

        curr_r = sr + step_hoi
        curr_c = sc + step_ver
        while curr_r != er: # 因為是斜角，檢查完 r, c 也到了
            if board[curr_r][curr_c] != " ":
                return False
            curr_r += step_hoi
            curr_c += step_ver


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

    
def valid_knight_move(board, sr, sc, er, ec):
    if abs(sr - er) * abs(sc - ec) != 2:
        return False

    return True


def valid_king_move(board, sr, sc, er, ec):
    if abs(sr - er) == 1 and abs(sc - ec) == 1:
        return True
    if abs(sr - er) + abs(sc - ec) > 1:
        return False
    return True
