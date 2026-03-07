# Improved Connect 4 Game

class Connect4:
    ROWS = 8
    COLS = 7

    def __init__(self):
        self.board = [[' ' for _ in range(self.COLS)] for _ in range(self.ROWS)]
        self.current_player = 'A'

    def switch_player(self):
        self.current_player = 'B' if self.current_player == 'A' else 'A'

    def print_board(self):
        print("\nCurrent Board:")
        for row in self.board:
            print('|', end='')
            for cell in row:
                if cell == 'A':
                    print('\033[91mA\033[0m', end='|')  # Red for A
                elif cell == 'B':
                    print('\033[94mB\033[0m', end='|')  # Blue for B
                else:
                    print(' ', end='|')
            print()
        print('---------------')
        print(' 1 2 3 4 5 6 7')

    def drop_chip(self, column):
        """Drop a chip in the chosen column (1-7)."""
        if not (1 <= column <= self.COLS):
            return False

        for row in range(self.ROWS - 1, -1, -1):
            if self.board[row][column - 1] == ' ':
                self.board[row][column - 1] = self.current_player
                return True
        return False

    def check_win(self, player):
        """Check if a player has 4 in a row (horizontal, vertical, diagonal)."""
        # Horizontal check
        for row in range(self.ROWS):
            for col in range(self.COLS - 3):
                if all(self.board[row][col + i] == player for i in range(4)):
                    return True

        # Vertical check
        for row in range(self.ROWS - 3):
            for col in range(self.COLS):
                if all(self.board[row + i][col] == player for i in range(4)):
                    return True

        # Diagonal (down-right)
        for row in range(self.ROWS - 3):
            for col in range(self.COLS - 3):
                if all(self.board[row + i][col + i] == player for i in range(4)):
                    return True

        # Diagonal (up-right)
        for row in range(3, self.ROWS):
            for col in range(self.COLS - 3):
                if all(self.board[row - i][col + i] == player for i in range(4)):
                    return True

        return False

    def is_full(self):
        """Check if the board is full."""
        return all(self.board[0][col] != ' ' for col in range(self.COLS))

    def play_game(self):
        """Main game loop."""
        print("Welcome to Connect 4!\n")
        while True:
            self.print_board()
            print(f"Player {self.current_player}'s turn.")

            try:
                column = int(input("Enter column (1-7): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 7.")
                continue

            if not self.drop_chip(column):
                print("Invalid move! Column is full or out of range. Try again.")
                continue

            if self.check_win(self.current_player):
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break

            if self.is_full():
                self.print_board()
                print("It's a tie! No more moves left.")
                break

            self.switch_player()


if __name__ == "__main__":
    game = Connect4()

    # __init__ test
    print("Testing __init__")
    print("Current player:", game.current_player)
    print("Board size:", len(game.board), "rows x", len(game.board[0]), "columns")
    game.print_board()

    # switch_player test
    print("\nTesting switch_player")
    print("Before switch:", game.current_player)
    game.switch_player()
    print("After first switch:", game.current_player)
    game.switch_player()
    print("After second switch:", game.current_player)

    # drop_chip test
    print("\nTesting drop_chip")
    print("Drop in column 1:", game.drop_chip(1))
    print("Drop in invalid column 0:", game.drop_chip(0))
    print("Drop in invalid column 8:", game.drop_chip(8))
    game.print_board()

    # check_win horizontal test
    print("\nTesting check_win (horizontal)")
    game2 = Connect4()
    game2.current_player = 'A'
    game2.drop_chip(1)
    game2.drop_chip(2)
    game2.drop_chip(3)
    game2.drop_chip(4)
    game2.print_board()
    print("Horizontal win for A:", game2.check_win('A'))

    # check_win vertical test
    print("\nTesting check_win (vertical)")
    game3 = Connect4()
    game3.current_player = 'A'
    for _ in range(4):
        game3.drop_chip(1)
    game3.print_board()
    print("Vertical win for A:", game3.check_win('A'))

    # check_win diagonal test
    print("\nTesting check_win (diagonal)")
    game4 = Connect4()
    game4.board[7][0] = 'A'
    game4.board[6][1] = 'A'
    game4.board[5][2] = 'A'
    game4.board[4][3] = 'A'
    game4.print_board()
    print("Diagonal win for A:", game4.check_win('A'))

    # is_full test
    print("\nTesting is_full")
    game5 = Connect4()
    print("Board full before filling:", game5.is_full())
    for col in range(1, game5.COLS + 1):
        for _ in range(game5.ROWS):
            game5.drop_chip(col)
    print("Board full after filling:", game5.is_full())


    #Connect4().play_game()