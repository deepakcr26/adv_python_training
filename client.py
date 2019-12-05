import socket
sd = socket.socket()
PORT = 7105

sd.connect(('127.0.0.1', PORT))

print(sd.recv(1024).decode())

sd.close()
