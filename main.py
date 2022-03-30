import eel
import socket
import time
import pandas as pd
import matplotlib.pyplot as plt

eel.init('web')
clien = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clien.connect(("127.0.0.1", 1265))

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

@eel.expose
def get_data():
    clien.send('get'.encode('utf-8'))  # отправляем режим для получения данных
    datafile = clien.recv(1024)

    data1 = datafile.decode('utf-8').split('@') #типа среднее за каждый день недели
    del data1[len(data1)-1]
    data1 = list(map(int, data1))
    #print(data1)

    s = pd.Series(data1)
    f1 = plt.figure(figsize=(6, 4))
    s.plot(kind='bar', xlabel='День', ylabel='Интенсивность освещенности')
    f1.savefig('web/static/plot1.png')

    s = pd.Series(data1)
    f2 = plt.figure(figsize=(6, 4))
    s.plot(kind='pie', xlabel='День', ylabel='Интенсивность освещенности')
    f2.savefig('web/static/plot2.png')
    return 0


eel.start('mian.html', size=(1200, 800))