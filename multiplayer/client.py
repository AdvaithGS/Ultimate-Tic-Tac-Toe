import socket
name = input('Enter player name: ')
host = '0.tcp.in.ngrok.io'
port = int(input('Enter port: '))

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((host,port))
socket.send(name.encode('utf-8'))
while True:
  a = str(socket.recv(1024).decode('utf-8'))
  if a.endswith('space'):
    a = a.replace('space','')
    print(a,end = ' ')
  elif a.endswith('input'):
    print()
    a = a.replace('input','')
    inp = input(a)
    socket.send(inp.encode('utf-8'))
  elif a == 'EXIT':
    break
  else:
    print(a)

