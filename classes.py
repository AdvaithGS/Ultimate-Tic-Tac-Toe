import termcolor
from json import loads,dumps
import os

if 'ut3.json' not in os.listdir():
  print()
  f = open('ut3.json','w')
  
  print ('Does the following line render properly for you? Y/N:', termcolor.colored('Ultimate Tic Tic Toe','yellow'),sep = '\n')
  s = input('>> ').lower()
  while s not in ['y','n']:
    s = input('>> ').lower()
  if s == 'y':
    d = {'color_compatible':True}
    d['self_colour'] = 'green'
    d['opponent_colour'] = 'yellow' 
  else:
    d = {'color_compatible':False}
  d['preferred_port'] = 5555
  d['online_self_colour'] = 'cyan'
  f.write(dumps(d))
  f.close()
with open('ut3.json') as f:
  d = loads(f.read())

def colored(s:str,c:str):
  if d['color_compatible']:
    return termcolor.colored(s,c)
  return s

class Player():
  def __init__(self,name: str,sign: str,colour : str):
    self.name = name
    self.colour = colour
    self.sign = sign
  def __str__(self):
    return self.name

class Board():
  def __init__(self,board:list  = [['-']*9 for i in range(9)],won:list = [' ' for i in range(9)], game_won = False):
    self.board = board
    self.won = won
    self.game_won = False
  def __str__(self):
    return self.board
  def show(self,connected = False,client = None):
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
    if connected:
      b = self.board
      s = f'''
{b[0][0]} {b[0][1]} {b[0][2]}  |  {b[1][0]} {b[1][1]} {b[1][2]}  |  {b[2][0]} {b[2][1]} {b[2][2]}
{b[0][3]} {b[0][4]} {b[0][5]}  |  {b[1][3]} {b[1][4]} {b[1][5]}  |  {b[2][3]} {b[2][4]} {b[2][5]}
{b[0][6]} {b[0][7]} {b[0][8]}  |  {b[1][6]} {b[1][7]} {b[1][8]}  |  {b[2][6]} {b[2][7]} {b[2][8]}

{b[3][0]} {b[3][1]} {b[3][2]}  |  {b[4][0]} {b[4][1]} {b[4][2]}  |  {b[5][0]} {b[5][1]} {b[5][2]}
{b[3][3]} {b[3][4]} {b[3][5]}  |  {b[4][3]} {b[4][4]} {b[4][5]}  |  {b[5][3]} {b[5][4]} {b[5][5]}
{b[3][6]} {b[3][7]} {b[3][8]}  |  {b[4][6]} {b[4][7]} {b[4][8]}  |  {b[5][6]} {b[5][7]} {b[5][8]}

{b[6][0]} {b[6][1]} {b[6][2]}  |  {b[7][0]} {b[7][1]} {b[7][2]}  |  {b[8][0]} {b[8][1]} {b[8][2]}
{b[6][3]} {b[6][4]} {b[6][5]}  |  {b[7][3]} {b[7][4]} {b[7][5]}  |  {b[8][3]} {b[8][4]} {b[8][5]}
{b[6][6]} {b[6][7]} {b[6][8]}  |  {b[7][6]} {b[7][7]} {b[7][8]}  |  {b[8][6]} {b[8][7]} {b[8][8]}
'''
      client.send(s.encode('utf-8'))
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
      self.game_won = True
      f = open('gamesave.ut3','wb')
      f.close()
      return colored(f'{player.name} has won the game! Congratulations',player.colour)
    return '\n'
 
