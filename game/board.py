class Board:
    def __init__(self):
        # 建立 8x8 空棋盤
        self.board = [[" " for _ in range(8)] for _ in range(8)]
        # 放黑棋
        self.board[0] = ["R","N","B","Q","K","B","N","R"]
        self.board[1] = ["P"]*8
        # 放白棋
        self.board[6] = ["p"]*8
        self.board[7] = ["r","n","b","q","k","b","n","r"]

    def print_board(self):
        print("  a b c d e f g h")
        for i, row in enumerate(self.board):
            print(8-i, " ".join(row), 8-i)
        print("  a b c d e f g h")


    def move_piece(self, move):
        """
        move: 字串，像 "e2 e4"
        功能: 將棋子從起點移到終點
        """
        start, end = move.split()  # 分割起點與終點
        start_col = ord(start[0]) - ord('a')  # a~h → 0~7
        start_row = 8 - int(start[1])         # 1~8 → 7~0
        end_col = ord(end[0]) - ord('a')
        end_row = 8 - int(end[1])

        # 移動棋子
        piece = self.board[start_row][start_col]
        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = " "

if __name__ == "__main__":
    b = Board()
    b.print_board()  # 印出初始棋盤

    while True:
        move = input("輸入移動 (格式: e2 e4, q 結束): ")
        if move.lower() == "q":
            break
        b.move_piece(move)  # 呼叫移動函數
        b.print_board()     # 更新後印出棋盤

