import socket
from random import randint
import time

clien = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clien.connect(("127.0.0.1", 1265))

data1 = [randint(1, 500) for i in range(7)]#типА средние за неделю
data3 = [randint(1, 500) for i in range(7)]#типА средние за пошлую неделю


def generate(data):
    l = ''
    for i in range(7):
        l += str(data[i]) + '@'
    return l


while True:
    data = clien.recv(1024)
    if data.decode('utf-8') == 'get':
        data2 = str(randint(1, 500))

        line2 = generate(data1)
        line3 = generate(data3)

        clien.send(data2.encode('utf-8'))
        time.sleep(0.01)
        clien.send(line2.encode('utf-8'))
        time.sleep(0.01)
        clien.send(line3.encode('utf-8'))


