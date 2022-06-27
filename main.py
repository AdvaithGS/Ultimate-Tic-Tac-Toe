from stat import S_ENFMT


s = input('Choose 1 for 2-player and 2 for multiplayer: ')
while not s.isdigit() or int(s) not in range(1,3):
  print('Input must be either 1 or 2')
s = int(s)

if s == 1:
  import two_player
elif s == 2:
  import multi_player