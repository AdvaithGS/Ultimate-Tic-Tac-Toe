import os
from classes import colored
import json

if 'ut3.json' not in os.listdir():
  print()
  f = open('ut3.json','w')
  
  print ('Does the following line render properly for you? Y/N:', colored('Ultimate Tic Tic Toe','yellow'),sep = '\n')
  s = input('>> ').lower()
  while s not in ['y','n']:
    s = input('>> ').lower()
  if s == 'y':
    d = {'color_compatible':True}
  else:
    d = {'color_compatible':False}

  f.write(json.dumps(d))
  f.close()

print(f"\t{colored('**********************************************','cyan')}")
print(f"\t{colored('***********  ','cyan')}{colored('Ultimate Tic Tac Toe','green')}{colored('  ***********','cyan')}")
print(f"\t{colored('**********************************************','cyan')}")

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