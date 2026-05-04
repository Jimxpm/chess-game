from game.rules import is_valid_move

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

        self.current_player = "white"  # 白棋先手
        self.game_over = False         # 遊戲狀態

    def print_board(self):
        #印出外圍標示(僅文字棋盤)
        print("  a b c d e f g h")
        for i, row in enumerate(self.board):
            print(8-i, " ".join(row), 8-i)
        print("  a b c d e f g h")


    def move_piece(self, move):
        if self.game_over:
            print("遊戲已結束")
            return
        """
        move: 字串，像 "e2 e4"
        功能: 將棋子從起點移到終點
        """
        start, end = move.split()  # 分割起點與終點
        start_col = ord(start[0]) - ord('a')  # a~h → 0~7, ord(a) 字母轉成ASCII
        start_row = 8 - int(start[1])         # 1~8 → 7~0
        end_col = ord(end[0]) - ord('a')
        end_row = 8 - int(end[1])

    
        #呼叫座標版的移動函式，執行 is_valid_move，檢驗移動合法性
        success = self.move_piece_by_coords((start_row, start_col), (end_row, end_col))

        if not success:
            print(f"移動指令 {move} 失敗：違反西洋棋規則！")
        else:
        # 如果成功，move_piece_by_coords做完
        # - 修改 self.board 陣列
        # - 換回合 (switch_turn)
            print(f"移動指令 {move} 成功執行。")


        #下列移至 move_piece_by_coords 操作
        #piece = self.board[start_row][start_col]

        #規則檢查
        #if piece == " ":
            #print("那裡沒有棋子！")
            #return

        # if self.current_player == "white" and piece.isupper():
        #     print("這不是你的棋子！")
        #     return
        # elif self.current_player == "black" and piece.islower():
        #     print("這不是你的棋子！")
        #     return
        # ----------------------

        #target = self.board[end_row][end_col]

        # # 吃 King 結束遊戲
        # if target.lower() == "k":
        #     print(self.current_player, "wins!")
        #     self.game_over = True

        # # 移動棋子
        # self.board[end_row][end_col] = piece
        # self.board[start_row][start_col] = " "

        # # 換回合
        # self.switch_turn()

    def switch_turn(self):
        #回合交換
        if self.current_player == "white":
            self.current_player = "black"
            print("現在是黑方回合")
        else:
            self.current_player = "white"    
            print("現在是白方回合")

    def move_piece_by_coords(self, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        
        #取得起始格子的棋子
        piece = self.board[start_row][start_col]
        
        # 防呆檢查 
        if piece == " ":
            return False # 點到空格，直接回傳失敗
            
        if (self.current_player == "white" and piece.isupper()) or \
           (self.current_player == "black" and piece.islower()):
            return False # 點到對手的棋子

        #規則判定
        if not is_valid_move(self.board, start_row, start_col, end_row, end_col):
            print(f"不合法的移動: {piece}")
            return False # 規則不通過，中斷移動

        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = " "
        self.switch_turn()
        return True 
    


