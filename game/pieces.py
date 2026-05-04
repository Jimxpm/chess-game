# game/pieces.py

def get_piece_type(piece):
    #取得棋子類別
    if piece == " ":
        return None
        
    # 建立字母到種類的字典
    piece_map = {
        'p': 'pawn',
        'r': 'rook',
        'n': 'knight',
        'b': 'bishop',
        'q': 'queen',
        'k': 'king'
    }
    
    # 統一轉成小寫來查詢
    return piece_map.get(piece.lower(), None)

def get_piece_color(piece):
    if piece == " ":
        return None
    return "black" if piece.isupper() else "white"