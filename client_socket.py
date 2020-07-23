import socket
import sys

s = socket.socket()

host = socket.gethostname()

port = 9999

s.connect(('127.0.0.1', port))

msg = s.recv(1024)

s.close()
print(msg.decode('utf-8'))
