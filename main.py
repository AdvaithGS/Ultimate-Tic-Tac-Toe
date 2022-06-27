from itertools import cycle
from termcolor import colored
from classes import Player,Board
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