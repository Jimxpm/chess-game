import pygame
import sys

# 常數設定
WIDTH, HEIGHT = 512, 512 # 8x8棋盤，每格 64x64
SQ_SIZE = WIDTH // 8

class PygameUI:
    def __init__(self, game_board):
        self.board_obj = game_board # 接收 game.board 的實例
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess Game")
        #self.font = pygame.font.SysFont("Arial", 32, bold=True)

        # 建立一個空字典存圖片
        self.images = {}
        self.load_images()
    
    def draw_board(self):
        colors = [pygame.Color(240, 217, 181), pygame.Color(181, 136, 99)] # 木紋配色
        for r in range(8):
            for c in range(8):
                color = colors[((r + c) % 2)] #決定這一格塗亮色還是暗色
                pygame.draw.rect(self.screen, color, pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                
                # 讀取棋盤狀態
                piece = self.board_obj.board[r][c] 
                if piece != " ":
                    # # 畫出文字棋子
                    # text_color = (0, 0, 0) if piece.isupper() else (255, 255, 255)
                    # text_surface = self.font.render(piece, True, text_color)
                    # self.screen.blit(text_surface, (c*SQ_SIZE + 20, r*SQ_SIZE + 15))

                    # 從字典拿出對應的圖片，貼到座標上
                    self.screen.blit(self.images[piece], pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

    def convert_coords_to_notation(self, row, col):
        """將 (6, 4) 這種座標轉換回 'e2' 這種字串"""
        cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        return f"{cols[col]}{8 - row}" #使用格式化字串

    def run(self):
        running = True
        selected_sq = None # 紀錄 (row, col)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    location = pygame.mouse.get_pos()
                    col = location[0] // SQ_SIZE
                    row = location[1] // SQ_SIZE
                    
                    if selected_sq == (row, col): # 點擊同一個地方，取消選取
                        selected_sq = None
                    elif selected_sq is None: # 第一次點擊：選取
                        if self.board_obj.board[row][col] != " ":
                            selected_sq = (row, col)
                    else: # 第二次點擊：嘗試移動
                        start_notation = self.convert_coords_to_notation(selected_sq[0], selected_sq[1])
                        end_notation = self.convert_coords_to_notation(row, col)
                        move_str = f"{start_notation} {end_notation}" # 組合出 "e2 e4"
                        
                        # 實際執行移動
                        self.board_obj.move_piece(move_str)
                        selected_sq = None

            # 更新畫面
            self.draw_board()
            
            # 加亮被選取的格子
            if selected_sq:
                r, c = selected_sq
                pygame.draw.rect(self.screen, (255, 0, 0), 
                                 pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE), 3)

            pygame.display.flip()
        
        pygame.quit()
        sys.exit()

    def load_images(self):
        """一次性將所有圖片載入記憶體，並調整成格子大小"""
        pieces = ['p', 'r', 'n', 'b', 'q', 'k']
        for piece in pieces:
            w_img = pygame.image.load(f"icon/w{piece}.png")
            # 縮放圖片以符合格子大小
            self.images[piece] = pygame.transform.scale(w_img, (SQ_SIZE, SQ_SIZE))
            
            b_img = pygame.image.load(f"icon/b{piece}.png")
            self.images[piece.upper()] = pygame.transform.scale(b_img, (SQ_SIZE, SQ_SIZE))