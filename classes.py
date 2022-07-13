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
  def show(self,connected = False,client = None):
    print()
    if connected:
      client.send('\n'.encode('utf-8'))
    for b in range(3):
      for a in range(3):
        for j in range(3):
          for i in range(3):
            print(self.board[j+3*b][i+3*a],end = ' ')
            if connected:
              client.send((str(self.board[j+3*b][i+3*a]) + 'space').encode('utf-8'))
          if j != 2:
            print(' | ', end = ' ')
            if connected:
              client.send((' | ' + 'space').encode('utf-8'))
        print()
        if connected:
          client.send(('\n').encode('utf-8'))
      print()
      if connected:
        client.send(('\n').encode('utf-8'))
  
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