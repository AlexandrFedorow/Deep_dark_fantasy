# Deep_dark_fantasy
Это приложенеиние создано для визуализации данных, получаемых компьютером от устройств умного дома. Для демонстрации работы программы был эмулирован датчик освещенности.
<br><br>Проект состоит из трех частей:
- Программа для компьютера. Она отображает данные с датчиков. Для визуализации и работы с данными были использованы библиотеки: matplotlib, pandas и numpy. Для создания графического интерфейса использовалась библиотека eel. Для общения с сервером использовалась библиотека socket.
- Сервер. Он создан для связи датчиков и компьютера и их проверки.
- Программа, эмулирующая работу датчика. Она генерирует случайные числа (условная степень освещенности помещения) и отправляет их на сервер.

## Принцип работы системы
<p>Клиент (программа на компьютере) для добавления датчика отправляет на сервер запрос в виде [тип режима + серийный номер датчика].<br>
Сервер проверяет серийный номер в базе данных (на данном этапе это txt файл), если такой номер существует, на клиентской части создется датчик.</p>
<p>Для получения данных, клиент отправляет на сервер запрос в виде [тип режима]. <br>
Сервер отпраляет датчику такой же запрос и ждет от него данные.<br>
Датчик принимает запрос и генерирует данные. До клиента они идут обратным путем.</p>

## Указания для запуска
Сначала запустите сервер, затем файл main.py, дождитесь открытия графического окна, затем запустите файл client2.p.<br>
Для добавления датчика используйте серийный номер "gg".

## Если не работает
Прилагаем видео, на котором представлена работа программы.<br>
https://disk.yandex.ru/i/87pq4wQa204Vyg

