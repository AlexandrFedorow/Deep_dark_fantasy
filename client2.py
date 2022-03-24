import socket
from random import randint

clien = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clien.connect(("127.0.0.1", 1235))

while True:
    data = clien.recv(1024)
    print(data.decode('utf-8'))
    #if data.decode('utf-8') == 'send':
    clien.send(str(randint(1, 100)).encode('utf-8'))