import os
from classes import colored
import json


print(f"\t{colored('**********************************************','yellow')}")
print(f"\t{colored('***********  ','yellow')}{colored('Ultimate Tic Tac Toe','white')}{colored('  ***********','yellow')}")
print(f"\t{colored('**********************************************','yellow')}")

print('Enter 1 to start playing and 2 for settings:')
s = input('>> ')
while not s.isdigit() or int(s) not in [1,2]:
  s = input('>> ')

if int(s) == 1:
  print('Choose 1 for 2-player and 2 for multiplayer: ')
  s = input('>> ')
  while not s.isdigit() or int(s) not in range(1,3):
    s = input('>> ')
  s = int(s)

  if s == 1:
    import two_player.two_player
  elif s == 2:
    import multiplayer.menu

else:
  os.popen('ut3.json')