import eel
import socket

eel.init('web')
#clien = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#clien.connect(("127.0.0.1", 1235))


@eel.expose
def call(device_name):
    print('gg')
    #clien.send('get'.encode('utf-8'))
    #data = clien.recv(1024)
    #print(data.decode('utf-8'))
    """if device_name == 'gg':
        return 1"""
    return 1


eel.start('mian.html', size=(1200, 800))