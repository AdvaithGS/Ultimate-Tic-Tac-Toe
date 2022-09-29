from itertools import cycle
import os
import pickle
from classes import Player,Board,colored
from json import loads

with open('ut3.json') as f:
  d = loads(f.read())

if not 'gamesave.ut3' in os.listdir():
  f = open('gamesave.ut3','wb')
  f.close()

with open('gamesave.ut3','rb') as f:
  if len(f.read()):
    f.seek(0,0)
    p1 = pickle.load(f)
    p2 = pickle.load(f)
    board = pickle.load(f)
    playing = pickle.load(f)
    choice = pickle.load(f)
    inp = input(f'Found a paused game between {p1.name} and {p2.name}. Do you wish to recover it?: Y/N >> ').lower()
    while not inp in ['y','n']:
      inp = input('>> ').lower()
    
    if inp != 'y':
      f = open('gamesave.ut3','wb')
      f.close()
      var = False
    else:
      var = True
  else:
    var = False  
if not var:
  p1 = Player(input('Enter player 1 (X) name: '),'X',d['self_colour'])
  p2 = Player(input('Enter player 2 (O) name: '),'O',d['opponent_colour'])
  board = Board()
  playing = 0
  choice = 4

board.show()
if playing:
  p1,p2 = p2,p1

gamers = cycle(iter([p1,p2]))

while not board.game_won:
  area = choice
  current_player : Player = next(gamers)
  print(f'Now it is {current_player}\'s chance.')
  playing = 0 if current_player == p1 else 1

  choice = input(f'Make your move, {current_player}: ')
  
  if choice == 'pause':
    with open('gamesave.ut3','wb') as f:
      for i in p1,p2,board,playing,area:
        pickle.dump(i,f)
    print('Game paused and saved to file.')
    break
  elif choice == 'exit':
    inp = input('Do you wish to save the game? Y/N >> ').lower()
    while inp not in ['y','n']:
      inp = input('>> ')
    if inp == 'y':
      with open('gamesave.ut3','wb') as f:
        for i in p1,p2,board,playing,area:
          pickle.dump(i,f)
      print('Game paused and saved to file.')
    break

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