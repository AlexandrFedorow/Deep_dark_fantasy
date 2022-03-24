import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 1235))

server.listen(2)
user1, adres1 = server.accept()
user2, adres2 = server.accept()
while True:
    #user1.send('send'.encode('utf-8'))
    data_user1 = user1.recv(1024)
    #print(data.decode('utf-8'))
    user2.send(data_user1)

    data_user2 = user2.recv(1024)
    user1.send(data_user2)