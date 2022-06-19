from itertools import cycle
from termcolor import colored
class Player():
  def __init__(self,name: str,sign: str,wins: list):
    self.name = name
    self.sign = sign
    self.wins = wins
  def __str__(self):
    return self.name

p1 = Player(input('Enter player 1 (X) name: '),'X',[])
p2 = Player(input('Enter player 2 (O) name: '),'O',[])

board = [['-']*9 for i in range(9)]
def show():
  for b in range(3):
    for a in range(3):
      for j in range(3):
        for i in range(3):
          print(board[j+3*b][i+3*a],end = ' ')
        if j != 2:
          print(' | ', end = ' ')
      print()
    print()
show()
def game_won():
  pass
gamers = cycle(iter([p1,p2]))
choice  = 4
while not game_won():
  area = choice
  current_player : Player = next(gamers)
  print(f'Now it is {current_player}\'s chance.')
  choice = int(input(f'Make your move, {current_player}: ')) - 1
  while choice not in range(10) or all([i != '-' for i in board[choice]]) or board[area][choice] != '-':
    print(colored('Please choose a valid position that is not taken/allows the opponent to play','red'))
    choice = int(input(f'Make your move, {current_player}: ')) - 1
  board[area][choice] = current_player.sign
  show()
    
