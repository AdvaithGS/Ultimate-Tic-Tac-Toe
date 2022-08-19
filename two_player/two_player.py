from itertools import cycle
import termcolor

from classes import Player,Board,colored
from json import loads

with open('ut3.json') as f:
  d = loads(f.read())

p1 = Player(input('Enter player 1 (X) name: '),'X',d['self_colour'])
p2 = Player(input('Enter player 2 (O) name: '),'O',d['opponent_colour'])

board = Board()

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
  
  while choice not in range(9) or board.board[area][choice] != '-':
    print(colored('Please choose a valid position that is not taken/allows the opponent to play','red'))
    choice = int(input(f'Make your move, {current_player}: ')) - 1
  
  board.board[area][choice] = current_player.sign
  status = board.game_status(area,current_player)
  board.show()
  if status:
    print(status)
    print(board.check_game(current_player))
  if not board.game_won and all([i != '-' for i in board.board[choice]]):
    next_player = next(gamers)
    print(f'{current_player.name} has chosen a square that is full, so {next_player.name} can choose any square to play.')
    area = input(f'{next_player}, chose the square in which you want to play: ')

    while not area.isdigit() or int(area) not in range(10) or all([i == '-' for i in board.board[int(area)]]):
      area = input(('Chose a valid square: ','red'))
    player_skip = next(gamers)
    choice = int(area) - 1