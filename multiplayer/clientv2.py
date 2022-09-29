import socket
name = input('Enter player name: ')
host = input('Enter ip of host: ')
port = 5555

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((host,port))
socket.send(name.encode('utf-8'))

while True:
  a = str(socket.recv(1024).decode('utf-8'))
  print(a)
  if a == 'Thank you!':
    break