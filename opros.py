import serial
import minimalmodbus
from tkinter import messagebox
import csv
import time
import re

list_modules = []  # хранилище адресов всех найденых модулей
list_command = []  # хранилище всех команд на которые отвечают найденные модули
list_modules_command_vkl = []  # хранилище команд для включения или выключения
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
    port_open = serial.Serial('com{}'.format(port), 115200, timeout=0.1, stopbits=1, bytesize=8)  # для ардуино
                                                # stopbits=1, bytesize=8 для всего остального stopbits=2, bytesize=7


def find_module():
    global list_modules
    global answers
    global active_module
    global list_command
    global list_modules_command_vkl
    if input('Выполниить поиск модулей (Y/N):') == 'Y':
        for i in range(128, 160):
            LRC = hex(ord(minimalmodbus._calculateLrcString(hex(i)[2:].upper() + '445100000005')))[2:]
            message = ':' + hex(i)[2:].upper() + '445100000005' + LRC.upper() + '\r\n'
            print(message)
            port_open.write(message.encode('ascii'))
            otvet = repr(port_open.read(115))[1:]
            print(otvet)
            if len(otvet) > 100:
                list_modules += [otvet[2:4]]
                active_module += [False]
                list_command += ['51']
                list_modules_command_vkl += ['00000005']
                answers += [otvet]
            else:
                LRC = hex(ord(minimalmodbus._calculateLrcString(hex(i)[2:].upper() + '4449000000')))[2:]
                message = ':' + hex(i)[2:].upper() + '4449000000' + LRC.upper() + '\r\n'
                print(message)
                port_open.write(message.encode('ascii'))
                otvet = repr(port_open.read(80))[1:]
                print(otvet)
                if len(otvet) > 55:
                    list_modules += [otvet[2:4]]
                    active_module += [False]
                    list_command += ['49']
                    list_modules_command_vkl += ['000000']
                    answers += [otvet]
                else:
                    LRC = hex(ord(minimalmodbus._calculateLrcString(hex(i)[2:].upper() + '4447000000')))[2:]
                    message = ':' + hex(i)[2:].upper() + '4447000000' + LRC.upper() + '\r\n'
                    print(message)
                    port_open.write(message.encode('ascii'))
                    otvet = repr(port_open.read(120))[1:]
                    print(otvet)
                    if len(otvet) > 10:
                        list_modules += [otvet[2:4]]
                        active_module += [False]
                        list_command += ['47']
                        list_modules_command_vkl += ['000000']
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
    else:                         # загрузим из файла предыдущий поиск модулей и их конфигурацию
        massive = []
        with open('config.csv', newline='') as file:
            adresses_commands = csv.reader(file)
            for row in adresses_commands:
                massive += [row]  # передадим пустому массиву строки с данными из файла
            list_modules += massive[0]  # запишем в массив адресов первую строку из файла
            list_command += massive[1]  # запишем в массив команд модулей вторую строку из файла
            list_modules_command_vkl += massive[2]  # запишем в массив команд вкл/выкл третью строку из файла
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
                ans = repr(port_open.read(120))#[1:]
                try:  # попытка отсеить лишние байты перед двоеточием
                    # ans = 'b' + ans[ans.index(':'):]
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
