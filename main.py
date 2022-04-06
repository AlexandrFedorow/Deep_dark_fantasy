import eel
import socket
import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import config

eel.init('web')
clien = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clien.connect(("127.0.0.1", 1265))


@eel.expose
def call(device_name):
    clien.send('check'.encode('utf-8'))    #отправляем режим для проверки в базе
    time.sleep(0.01)
    clien.send(device_name.encode('utf-8'))#отправляем серийый номер

    check = clien.recv(1024)
    #print(check.decode('utf-8'))
    if check.decode('utf-8') == '1':
        return 1
    else:
        return 0


@eel.expose
def get_data():
    day = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс'] #тут типа дни недели

    x1 = np.arange(1, 8) - 0.2
    x2 = np.arange(1, 8) + 0.2

    clien.send('get'.encode('utf-8'))  # отправляем режим для получения данных
    datafile1 = clien.recv(1024)
    datafile2 = clien.recv(1024)
    datafile3 = clien.recv(1024)

    if config.HOUR_CTR < 23:
        config.data.append(int(datafile1.decode('utf-8')))
        config.HOUR_CTR += 1

    data2 = datafile2.decode('utf-8').split('@')  # типа среднее за каждый день недели
    data3 = datafile3.decode('utf-8').split('@')  # типа среднее за каждый день прошлой недели

    del data2[len(data2) - 1]
    data2 = list(map(int, data2))

    del data3[len(data3) - 1]
    data3 = list(map(int, data3))

    ss = pd.Series(int(datafile1.decode('utf-8')), [''])  # график момента
    f2 = plt.figure(figsize=(6, 4))
    ss.plot(kind='bar', title="Освещенность сейчас", ylim=(None, 500), ylabel='Интенсивность освещенности', width=0.1)
    f2.savefig('web/static/plot0.png')

    s = pd.Series(data2, day) #график недели
    f1 = plt.figure(figsize=(6, 4))
    s.plot(kind='bar', ylim=(None, 500), ylabel='Интенсивность освещенности', title="Освещенность на этой неделе")
    plt.xticks(rotation=360)
    f1.savefig('web/static/plot1.png')

    fig, ax = plt.subplots()  #график зависимости по неделям
    ax.bar(x1, data2, width=0.4)
    ax.bar(x2, data3, width=0.4)
    ax.set_xticklabels(['пн']+day)
    ax.set_title('Освещенность отностельно прошлой недели')
    fig.set_figwidth(6)  # ширина Figure
    fig.set_figheight(4)  # высота Figure
    fig.savefig('web/static/plot2.png')

    s = pd.Series(config.data) #график по часам
    f3 = plt.figure(figsize=(6, 4))
    s.plot(xlabel='Время', ylim=(None, 500), xlim=(0, 23), ylabel='Интенсивность освещенности',  title="Освещенность за день", marker='o')
    f3.savefig('web/static/plot3.png')
    
    return 0


eel.start('mian.html', size=(1200, 800))