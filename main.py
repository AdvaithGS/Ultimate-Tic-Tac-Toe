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
  def game_status(self,choice : int, current_player : Player):
    if self.won[choice] != ' ':
      return
    l = [0,1,2,3,6,0,2,0]
    #   [4,3,2,1,1,3,3,1]
    for i in range(len(l)):
      if i < 5:
        cursor = max(4-l[i],1) 
      else:
        cursor = 8-i + (l[i]//2)
      if all([self.board[choice][j] == current_player.sign for j in range(l[i],l[i] + (2*cursor) + 1,cursor)]):
        self.won[choice] = current_player.name
        for j in range(l[i],l[i] + (2*cursor) + 1,cursor):
          self.board[choice][j] = colored(self.board[choice][j],current_player.colour)
        return colored(f'{current_player.name} has taken square {choice + 1}. ',current_player.colour)
    else:
      return
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
