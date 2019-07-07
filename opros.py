import serial
import minimalmodbus
from tkinter import messagebox
import csv
import time
import re

list_modules = []  # хранилище адресов всех найденых модулей
list_command = []  # хранилище всех команд на которые отвечают найденные модули
list_command_buffer = []  # буфер команд. Нужен для сохранения изначальных команд если захочется модули опрашивать 51 командой.
list_modules_command_vkl = []  # хранилище команд для включения или выключения
list_modules_command_vkl_buffer = []  # буфер запросов на модуль. Нужен для сохранения изначальных запросных байтов если захочется модули опрашивать 51 командой.
active_module = []  # хранилище флагов выбранных галочками модулей
answers = []  # хранилище ответов от модулей
active_parametrs = [True, True, True]  # хранилище значений галочек вкл свч, вкл ип, вкл питание
flag_on_opros = True  # флаг активного обмена или паузы
flag_sbros_avrii = False
mask = re.compile(r':.+?(\\r\\n)')  #маска для выделения сообщения из мусора


def find_port():
    global port_open
    port = 0
    ports = dict()
    for number_port in range(10):
        try:
            i = serial.Serial('com{}'.format(number_port), 115200, timeout=1, stopbits=2, bytesize=7)
            ports[number_port] = ('com{}'.format(number_port))
            i.close()
        except serial.serialutil.SerialException:
            pass
    if len(ports) == 0:
        messagebox.showinfo('Ахтунг!', message='Отсутствуют сом-порты')
        exit()
    elif len(ports) > 1:
        print(ports)
        port = int(input('Выберите нужный порт:'))
    elif len(ports) == 1:
        port = str(ports.keys())[11:12]  # port.keys возвращает что-то типа (dict_keys([2])).
        # это надо перевести в строку, затем извлечь слайсом двойку
        # и передать двойку в port
    port_open = serial.Serial('com{}'.format(port), 115200, timeout=0.1, stopbits=2, bytesize=7)  # для ардуино
                                                # stopbits=1, bytesize=8 для всего остального stopbits=2, bytesize=7


def find_module():
    global list_modules
    global answers
    global active_module
    global list_command
    global list_modules_command_vkl
    global list_command_buffer
    global list_modules_command_vkl_buffer
    if choise_start == 2:  # предложение выбора как искать модули. по запросу ID или по старинке 51, 49, 47
        for i in range(128, 160):
            LRC = hex(ord(minimalmodbus._calculateLrcString(hex(i)[2:].upper() + '2B0E0405')))[2:]  # Запрашиваем по всему диапазону адресов тип модуля через ID
            message = ':' + hex(i)[2:].upper() + '2B0E0205' + LRC.upper() + '\r\n'                  # 2В0Е - команда для чтения ID, 02 - тип доступа, 05 - запрос на количество каналов и частот
            print(message)
            port_open.write(message.encode('ascii'))
            ans = repr(port_open.read(100))
            try:  # попытка найти в мусоре ответ от нужного модуля
                ans = mask.search(ans).group()
            except:
                ans = 'adress {} - no module'.format(hex(i))
            print(ans)
            if ans[0] == ':' and ans[-1] == 'n' and ans[-3] == 'r' and int(hex(ord(minimalmodbus._calculateLrcString(ans[1:-6])))[2:].upper(), 16) == int(ans[-6:-4], 16):
                otvet = 'b' + ans  # тут б для того чтобы удобно было выбирать байты из ответов
                list_modules += [otvet[2:4]]
                active_module += [False]
                if int(otvet[26]) == 1:
                    list_command += ['47']
                    list_modules_command_vkl += ['000000']
                    list_command_buffer += ['47']  # к буферу мы обратимся если поопрашиваем модуль 51 командой, а потом решим обратно поопрашивать 47 или 49 командами.
                    list_modules_command_vkl_buffer += ['000000']
                elif int(otvet[26]) == 2:
                    list_command += ['49']
                    list_modules_command_vkl += ['000000']
                    list_command_buffer += ['49']
                    list_modules_command_vkl_buffer += ['000000']
                elif int(otvet[26]) == 4:
                    list_command += ['51']
                    list_modules_command_vkl += ['00000005']
                    list_command_buffer += ['51']
                    list_modules_command_vkl_buffer += ['00000005']
                answers += [otvet]
        open('config.csv', 'w').close()  # после поиска всех модулей запишем результат в csv файл
        print(answers)  # 1. очистим старый файл
        for i in range(len(answers)):  # сократим ответы от модулей до двух символов
            answers[i] = answers[i][2:4]
        with open('config.csv', 'w', newline='') as file:  # откроем файл за запись и запишем 4 массива
            file_write = csv.writer(file)
            file_write.writerow(list_modules)
            file_write.writerow(list_command)
            file_write.writerow(list_modules_command_vkl)
            file_write.writerow(answers)
        print(list_modules)
        print(list_command)
    elif choise_start == 1:  # поиск модулей старым способом (51, 49, 47)
        for i in range(128, 160):
            LRC = hex(ord(minimalmodbus._calculateLrcString(hex(i)[2:].upper() + '445100000005')))[2:]
            message = ':' + hex(i)[2:].upper() + '445100000005' + LRC.upper() + '\r\n'
            print(message)
            port_open.write(message.encode('ascii'))
            otvet = repr(port_open.read(115))[1:]
            try:  # попытка найти в мусоре ответ от нужного модуля
                otvet = mask.search(otvet).group()
            except:
                otvet = ''
            print(otvet)
            if len(otvet) > 100:
                list_modules += [otvet[1:3]]
                active_module += [False]
                list_command += ['51']
                list_modules_command_vkl += ['00000005']
                list_command_buffer += ['51']
                list_modules_command_vkl_buffer += ['00000005']
                answers += [otvet]
            else:
                LRC = hex(ord(minimalmodbus._calculateLrcString(hex(i)[2:].upper() + '4449000000')))[2:]
                message = ':' + hex(i)[2:].upper() + '4449000000' + LRC.upper() + '\r\n'
                print(message)
                port_open.write(message.encode('ascii'))
                otvet = repr(port_open.read(80))[1:]
                try:  # попытка найти в мусоре ответ от нужного модуля
                    otvet = mask.search(otvet).group()
                except:
                    otvet = ''
                print(otvet)
                if len(otvet) > 55:
                    list_modules += [otvet[1:3]]
                    active_module += [False]
                    list_command += ['49']
                    list_modules_command_vkl += ['000000']
                    list_command_buffer += ['49']
                    list_modules_command_vkl_buffer += ['000000']
                    answers += [otvet]
                else:
                    LRC = hex(ord(minimalmodbus._calculateLrcString(hex(i)[2:].upper() + '4447000000')))[2:]
                    message = ':' + hex(i)[2:].upper() + '4447000000' + LRC.upper() + '\r\n'
                    print(message)
                    port_open.write(message.encode('ascii'))
                    otvet = repr(port_open.read(120))[1:]
                    try:  # попытка найти в мусоре ответ от нужного модуля
                        otvet = mask.search(otvet).group()
                    except:
                        otvet = ''
                    print(otvet)
                    if len(otvet) > 10:
                        list_modules += [otvet[1:3]]
                        active_module += [False]
                        list_command += ['47']
                        list_modules_command_vkl += ['000000']
                        list_command_buffer += ['47']  # к буферу мы обратимся если поопрашиваем модуль 51 командой, а потом решим обратно поопрашивать 47 или 49 командами.
                        list_modules_command_vkl_buffer += ['000000']
                        answers += [otvet]
        open('config.csv', 'w').close()  # после поиска всех модулей запишем результат в csv файл
        print(answers)  # 1. очистим старый файл
        for i in range(len(answers)):  # сократим ответы от модулей до двух символов
            answers[i] = answers[i][2:4]
        with open('config.csv', 'w', newline='') as file:  # откроем файл за запись и запишем 4 массива
            file_write = csv.writer(file)
            file_write.writerow(list_modules)
            file_write.writerow(list_command)
            file_write.writerow(list_modules_command_vkl)
            file_write.writerow(answers)
        print(list_modules)
        print(list_command)
    elif choise_start == 3:                         # загрузим из файла предыдущий поиск модулей и их конфигурацию
        massive = []
        with open('config.csv', newline='') as file:
            adresses_commands = csv.reader(file)
            for row in adresses_commands:
                massive += [row]  # передадим пустому массиву строки с данными из файла
            list_modules += massive[0]  # запишем в массив адресов первую строку из файла
            list_command += massive[1]  # запишем в массив команд модулей вторую строку из файла
            list_modules_command_vkl += massive[2]  # запишем в массив команд вкл/выкл третью строку из файла
            list_command_buffer = list_command[:]  # сконфигурируем массивы буферов
            list_modules_command_vkl_buffer = list_modules_command_vkl[:] # вот этот хитрый знак вконце создаёт именно копию списка(новый объёкт в памяти программы), а не ссылку на область памяти
            answers += massive[3] # сконфигурируем массив для ответов модулей
            for i in range(len(list_modules)):
                active_module += [False] # сконфигурируем массив для активных модулей
            print(list_modules)
            print(list_command)


def obmen():
    global list_modules
    global list_command
    global answers
    global flag_on_opros
    global flag_sbros_avrii
    while True:
        if flag_on_opros is True:
            for i in range(len(list_modules)):
                LRC = hex(ord(minimalmodbus._calculateLrcString(list_modules[i] + '44' + list_command[i] +
                                                                list_modules_command_vkl[i])))[2:]
                message = ':' + list_modules[i] + '44' + list_command[i] + list_modules_command_vkl[i] + \
                          LRC.upper() + '\r\n'
                print(message)
                port_open.write(message.encode('ascii'))
                ans = repr(port_open.read(120))
                try:  # попытка найти в мусоре ответ от нужного модуля
                    ans = mask.search(ans).group()
                except:
                    ans = 'not correct'
                print(ans)
                if ans[0] == ':' and ans[-1] == 'n' and ans[-3] == 'r':
                    if int(hex(ord(minimalmodbus._calculateLrcString(ans[1:-6])))[2:].upper(), 16) == int(ans[-6:-4], 16):
                        answers[i] = 'b' + ans  # тут б для того чтобы удобно было выбирать байты из ответов
                    else:
                        answers[i] = ''
                else:
                    answers[i] = ''
                    print(answers[i])
                if flag_sbros_avrii is True:
                    sbros_avarii()
        else:
            time.sleep(0.1)  # чтобы не зависало окно


def sbros_avarii():
    global flag_sbros_avrii
    for i in range(len(list_modules)):
        LRC = hex(ord(minimalmodbus._calculateLrcString(list_modules[i] + '050201FF00')))[2:]
        message = ':' + list_modules[i] + '050201FF00' + LRC.upper() + '\r\n'
        port_open.write(message.encode('ascii'))
        print(repr(port_open.read(120))[1:])
    flag_sbros_avrii = False


def return_ansver():
    return answers


if __name__ == '__main__':
    pass
