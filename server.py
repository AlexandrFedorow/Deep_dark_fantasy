import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 1265))

server.listen(2)
user1, adres1 = server.accept()
user2, adres2 = server.accept()
in_use = []
file = open('nuber_data.txt', 'r')  # тут будет файл со всесеми номерами (потом он будет scv)
line = file.read().split('\n')  # получаем все серийники

while True:
    data_user1 = user1.recv(1024)   # принимаем режим

    if data_user1.decode('utf-8') == 'check':
        device_name = user1.recv(1024)

        if device_name.decode('utf-8') in line and not(device_name.decode('utf-8') in in_use):
            in_use.append(device_name.decode('utf-8'))
            user1.send('1'.encode('utf-8'))  # возвращаем 1 если проверка прошла
        else:
            user1.send('0'.encode('utf-8'))  # возвращаем 0 если проверка не прошла
            
    elif data_user1.decode('utf-8') == 'get':
        user2.send(data_user1)
    
        data_user21 = user2.recv(1024)
        data_user22 = user2.recv(1024)
        data_user23 = user2.recv(1024)

        user1.send(data_user21)
        time.sleep(0.01)
        user1.send(data_user22)
        time.sleep(0.01)
        user1.send(data_user23)

    else:
        user1.send('0'.encode('utf-8'))

