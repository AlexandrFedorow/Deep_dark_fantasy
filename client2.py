import socket
from random import randint

clien = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clien.connect(("127.0.0.1", 1234))
file = open('device_data.txt', 'r')
while True:
    data = clien.recv(1024)
    if data.decode('utf-8') == 'get':
        clien.send(file)#тут должен высылаться файл (возможно csv)
