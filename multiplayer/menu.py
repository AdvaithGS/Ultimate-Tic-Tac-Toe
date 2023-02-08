import os
s = input('Do you want to host or join an existing match? 1:host, 2:join -')
while not s.isdigit() or int(s) not in [1,2]:
  s = input('Do you want to host or join an existing match? 1:host, 2:join -')
s = int(s)
if s == 1:
  import multiplayer.multiplayer
elif s == 2:
  import multiplayer.client