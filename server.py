import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 1234))

server.listen(2)
user1, adres1 = server.accept()
user2, adres2 = server.accept()
file = open('nuber_data.txt', 'r')  # тут будет файл со всесеми номерами (потом он будет scv)
line = file.read().split('\n')  # получаем все серийники (нужноподключить pndas)
while True:
    # user1.send('send'.encode('utf-8'))
    data_user1 = user1.recv(1024)   # принимаем режим
    print(data_user1.decode('utf-8'))

    if data_user1.decode('utf-8') == 'check':
        device_name = user1.recv(1024)
        if device_name.decode('utf-8') in line:   # тут будет нормальная проверка номера
            user1.send('1'.encode('utf-8')) # возвращаем 1 если проверка прошла
        else:
            user1.send('0'.encode('utf-8')) # возвращаем 0 если проверка не прошла
            
    elif data_user1.decode('utf-8') == 'get':
        user2.send(data_user1)
    
        data_user2 = user2.recv(1024)
        user1.send(data_user2)

    else:
        user1.send('0'.encode('utf-8'))

