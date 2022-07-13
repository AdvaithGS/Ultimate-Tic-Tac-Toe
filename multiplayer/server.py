import socket
host = socket.gethostbyname(socket.gethostname()) 
port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))

server.listen(5)
print(f'Listening on {socket.gethostbyname(socket.gethostname())}')

while True:
  player, address  = server.accept()
  name = player.recv(1024).decode('utf-8')
  print(f'{name} has connected through {address} Starting the game.')
  message = player.recv(1024).decode('utf-8')
  print(f'Message from client is : {message}')
  player.send('Thank you!'.encode('utf-8'))
  player.close()
  print(f'Closed.')
  break