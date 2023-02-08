import socket
import time
name = input('Enter player name: ')

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((input('Enter ip: '),int(input('Enter port: '))))
socket.send(name.encode('utf-8'))

while True:
  time.sleep(3)
  socket.send('Hello'.encode('utf-8'))
  a = str(socket.recv(1024).decode('utf-8'))
  print(a)
  if a == 'Thank you!':
    break