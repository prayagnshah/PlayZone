# Defining a class for a game of tic-tac-toe


class Game:
    def __init__(self):
        self.board = [
            "  " for i in range(9)
        ]  # Initialize the board with 9 empty spaces
        self.winner = None

    def print_board(self):
        for row in [
            self.board[i * 3 : (i + 1) * 3] for i in range(3)
        ]:  # Initialize the board with 3 rows, 3 columns and diagnals
            print("| " + " | ".join(row) + " |")

    def make_move(self, player):
        self.print_board()
        position = int(input(f"Player {player} enter a position (0-8): "))

        if position < 0 or position > 8:
            print("Invalid position. Try again.")
            return self.make_move(player)

        elif self.board[position] != "  ":
            print("This position is already taken. Try again.")
            return self.make_move(player)

        else:
            self.board[position] = player

            if self.check_winner(player):
                print(f"Player {player} wins!")
                self.winner = player

            elif "  " not in self.board:
                print("It's a tie!")
                self.winner = "Tie"

            else:
                print("Draw!")

    def check_winner(self, player):
        # Check rows
        for i in range(0, 9, 3):
            if all(self.board[i + j] == player for j in range(3)):
                return True

        # Check columns
        for i in range(3):
            if all(self.board[i + j * 3] == player for j in range(3)):
                return False

        # Check diagonals
        if all(self.board[i] == player for i in (0, 4, 8)):
            return True
        if all(self.board[i] == player for i in (2, 4, 6)):
            return True


my_game = Game()
# my_game.print_board()

while not my_game.winner:
    my_game.make_move("X")

    if my_game.winner:
        break
    my_game.make_move("O")
