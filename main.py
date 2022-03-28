import eel
import socket
import time

eel.init('web')
clien = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clien.connect(("127.0.0.1", 1234))


@eel.expose
def call(device_name):
    clien.send('check'.encode('utf-8'))    #отправляем режим для проверки в базе
    time.sleep(0.01)
    clien.send(device_name.encode('utf-8'))#отправляем серийый номер

    check = clien.recv(1024)
    print(check.decode('utf-8'))
    if check.decode('utf-8') == '1':
        return 1
    else:
        return 0


eel.start('mian.html', size=(1200, 800))