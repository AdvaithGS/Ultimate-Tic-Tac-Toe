from itertools import cycle
from termcolor import colored
class Player():
  def __init__(self,name: str,sign: str,colour : str):
    self.name = name
    self.colour = colour
    self.sign = sign
  def __str__(self):
    return self.name

class Board():
  def __init__(self,board:list ,won:list = [' ' for i in range(9)], game_won = False):
    self.board = board
    self.won = won
    self.game_won = False
  def __str__(self):
    return self.board
  def show(self):
    print()
    for b in range(3):
      for a in range(3):
        for j in range(3):
          for i in range(3):
            print(self.board[j+3*b][i+3*a],end = ' ')
          if j != 2:
            print(' | ', end = ' ')
        print()
      print()
  
  def check_list(self,board: list, sign :str):
    for i in [(0,4),(1,3),(2,2),(3,1),(6,1),(0,3),(2,3),(0,1)]:
      if all([board[j] == sign for j in range(i[0],i[0]+(2*i[1]) + 1,i[1]) ]):
        return True,i
    return False,(0,0)
  
  def game_status(self,choice : int, current_player : Player):
    if self.won[choice] != ' ':
      return
    if self.check_list(self.board[choice],current_player.sign)[0]:
      self.won[choice] = current_player.name
      i = self.check_list(self.board[choice],current_player.sign)[1]
      for j in range(i[0],i[0] + (2*i[1]) + 1,i[1]):
        self.board[choice][j] = colored(self.board[choice][j],current_player.colour)
      return colored(f'{current_player.name} has taken square {choice + 1}. ',current_player.colour)
    return
  
  def check_game(self,player : Player):
    if self.check_list(self.won,player.name)[0]:
      print(colored(f'{player.name} has won the game! Congratulations',player.colour))
      self.game_won = True
p1 = Player(input('Enter player 1 (X) name: '),'X','cyan')
p2 = Player(input('Enter player 2 (O) name: '),'O','yellow')

board = Board([['-']*9 for i in range(9)])

board.show()
gamers = cycle(iter([p1,p2]))
choice  = 4
while not board.game_won:
  area = choice
  current_player : Player = next(gamers)
  print(f'Now it is {current_player}\'s chance.')

  choice = input(f'Make your move, {current_player}: ')
  while not choice.isdigit():
    print('You must enter a number')
    choice = input(f'Make your move, {current_player}: ')
  choice = int(choice) - 1
  
  while choice not in range(10) or all([i != '-' for i in board.board[choice]]) or board.board[area][choice] != '-':
    print(colored('Please choose a valid position that is not taken/allows the opponent to play','red'))
    choice = int(input(f'Make your move, {current_player}: ')) - 1

  board.board[area][choice] = current_player.sign
  status = board.game_status(area,current_player)
  board.show()
  if status:
    print(status)
    board.check_game(current_player)