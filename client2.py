import socket
from random import randint

clien = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clien.connect(("127.0.0.1", 1265))

while True:
    data = clien.recv(1024)
    if data.decode('utf-8') == 'get':
        l = ''
        data2 = [randint(1, 20) for i in range(7)]
        for i in range(7):
            l += str(data2[i])+'@'
        clien.send(l.encode('utf-8'))#тут должен высылаться файл (возможно csv)


