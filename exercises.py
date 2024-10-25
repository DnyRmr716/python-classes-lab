def welcome_message():
    print("Welcome to Tic-Tac-Toe!")


class Game:
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def print_board(self):
        b = self.board
        print(f"""
          A   B   C
      1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
          ----------
      2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
          ----------
      3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if self.tie:
            print("It's a tie!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        while True:
            move = input(f"Player {self.turn}, enter a move (example: A1): ").lower()
            if move in self.board and self.board[move] is None:
                self.board[move] = self.turn
                break
            else:
                print("Invalid move. The cell is either taken or does not exist. Try again.")

    def check_for_winner(self):
        winning_combinations = [
            ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'],
            ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'],
            ['a1', 'b2', 'c3'], ['a3', 'b2', 'c1']
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == self.turn:
                self.winner = self.turn
                return True
        return False

    def check_for_tie(self):
        if all(value is not None for value in self.board.values()) and not self.winner:
            self.tie = True
            return True
        return False

    def switch_turn(self):
        self.turn = {'X': 'O', 'O': 'X'}[self.turn]

    def play_game(self):
        print("Shall we play a game?")
        while not self.winner and not self.tie:
            self.render()
            self.get_move()
            if self.check_for_winner():
                break
            if self.check_for_tie():
                break
            self.switch_turn()
        self.render()


if __name__ == "__main__":
    game = Game()
    game.play_game()
