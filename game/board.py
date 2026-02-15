class Board:
    def __init__(self):
        # 建立 8x8 空棋盤
        self.board = [[" " for _ in range(8)] for _ in range(8)]

    def print_board(self):
        print("  a b c d e f g h")
        for i, row in enumerate(self.board):
            print(8-i, " ".join(row), 8-i)
        print("  a b c d e f g h")

if __name__ == "__main__":
    b = Board()
    b.print_board()
