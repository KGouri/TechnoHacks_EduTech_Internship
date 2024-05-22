class TicTacToe:
  def __init__(self):
      self.board = [' '] * 9
      self.current_player = 'X'

  def display_board(self):
      print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
      print("---------")
      print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
      print("---------")
      print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

  def get_player_move(self):
      move = input(f"Player {self.current_player}, enter your move (1-9): ")
      return int(move) - 1

  def is_valid_move(self, move):
      return 0 <= move < 9 and self.board[move] == ' '

  def make_move(self, move):
      self.board[move] = self.current_player

  def check_winner(self):
      winning_combinations = [
          (0, 1, 2), (3, 4, 5), (6, 7, 8),
          (0, 3, 6), (1, 4, 7), (2, 5, 8),
          (0, 4, 8), (2, 4, 6)
      ]
      for combo in winning_combinations:
          if all(self.board[i] == self.current_player for i in combo):
              return True
      return False

  def play_game(self):
      while True:
          self.display_board()
          move = self.get_player_move()
          if self.is_valid_move(move):
              self.make_move(move)
              if self.check_winner():
                  print(f"Player {self.current_player} wins!")
                  break
              elif ' ' not in self.board:
                  print("The game ends in a tie!")
                  break
              else:
                  self.current_player = 'O' if self.current_player == 'X' else 'X'
          else:
              print("Invalid move. Try again.")

if __name__ == "__main__":
  game = TicTacToe()
  game.play_game()
