import socket
from classes import Board,Player,colored
from itertools import cycle
import time
from json import loads
name = input('Enter your name: ')
p1 = Player(name,'X','yellow')


with open('ut3.json') as f:
  d = loads(f.read())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0',d['preferred_port']))

server.listen(5)
print(f'Listening on port {d["preferred_port"]}, share ngrok tcp url with the other player to have them join in.')
client, address  = server.accept()

def new_print(s):
  global client
  print(s)
  client.send(str(s).encode('utf-8'))

def new_input(s:str,online:bool):
  global client
  if online:
    time.sleep(1)
    client.send((str(s)+'input').encode('utf-8'))
    return client.recv(1024).decode('utf-8')
  return input(s)

name = client.recv(1024).decode('utf-8')
p2 = Player(name,'O','cyan') 
print(f'{name} has connected through {address}. Starting the game.')
client.send(f'You have been connected with {p1.name}'.encode('utf-8'))

board = Board()
board.show(True,client)
gamers = cycle(iter([p1,p2]))
choice  = 4

while not board.game_won:
  try:
    area = choice
    current_player : Player = next(gamers)
    new_print(f'Now it is {colored(current_player,current_player.colour)}\'s chance.')

    choice = new_input(f'Make your move, {colored(current_player,current_player.colour)}: ',current_player == p2)

    while not choice.isdigit():
      new_print('You must enter a number')
      choice = new_input(f'Make your move, {colored(current_player,current_player.colour)}: ',current_player == p2)
    choice = int(choice) - 1

    while choice not in range(9) or board.board[area][choice] != '-':
      new_print(colored('Please choose a valid position that is not taken/allows the opponent to play','red'))
      choice = int(new_input(f'Make your move, {colored(current_player,current_player.colour)}: '),current_player == p2) - 1

    new_print(f'Player {colored(current_player,current_player.colour)} has chosen {choice+1}')

    board.board[area][choice] = current_player.sign
    status = board.game_status(area,current_player)
    board.show(True,client)
    if status:
      new_print(status)
      new_print(board.check_game(current_player))
    if not board.game_won and all([i != '-' for i in board.board[choice]]):
      next_player = next(gamers)
      new_print(f'{colored(current_player,current_player.colour)} has chosen a square that is full, so {colored(next_player,next_player.colour)} can choose any square to play.')
      area = new_input(f'{colored(next_player,next_player.colour)}, choose the square in which you want to play: ',next_player == p2)

      while not area.isdigit() or int(area) not in range(10) or all([i == '-' for i in board.board[int(area)]]):
        area = new_input(colored('Chose a valid square: ','red'),next_player == p2)
      new_print(f'Player {colored(next_player,next_player.colour)} is going to play next in square {area}')
      player_skip = next(gamers)
      choice = int(area) - 1
  except:
    client.send('EXIT'.encode('utf-8'))
new_print('\nClosing connection.')
new_print('EXIT')
client.close()