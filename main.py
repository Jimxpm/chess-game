from game.board import Board
from ui.gui import PygameUI 

def main():
    game_logic = Board()
    ui = PygameUI(game_logic)
    ui.run()

if __name__ == "__main__":
    main()


