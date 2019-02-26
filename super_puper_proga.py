import tkinter
import opros
import param_module
import time
import threading

flag_cheks = True  # флаг для того чтобы ставить и снимать галочки на всех модулях
flag_vkl_vikl_active_module = False

opros.find_port()
opros.find_module()

number_of_modules = len(opros.list_modules)


def all_vum_use():
    global flag_cheks
    if flag_cheks is True:
        for j in range(1, number_of_modules + 1):
            globals()['check{}'.format(j)].select()
            opros.active_module[j - 1] = True
    else:
        for j in range(1, number_of_modules + 1):
            globals()['check{}'.format(j)].deselect()
            opros.active_module[j - 1] = False
    flag_cheks = not flag_cheks


def update_window():
    while True:
        ansvers = opros.return_ansver()
        for i in range(len(ansvers)):
            if len(ansvers[i]) < 10:
                globals()['work{}_opros'.format(i + 1)]['text'] = 'обмена нет'
                globals()['work{}_opros'.format(i + 1)]['fg'] = 'red'
                globals()['pitan{}_opros'.format(i + 1)]['text'] = '(.Y.)'
                globals()['pitan{}_opros'.format(i + 1)]['fg'] = 'red'
                globals()['mod{}_opros'.format(i + 1)]['text'] = '0_o'
                globals()['mod{}_opros'.format(i + 1)]['fg'] = 'red'
            else:
                if ansvers[i][6:8] == '47':
                    if ansvers[i][18:22] == '0007':
                        globals()['work{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['work{}_opros'.format(i + 1)]['fg'] = 'green'
                        globals()['pitan{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['pitan{}_opros'.format(i + 1)]['fg'] = 'green'
                        globals()['mod{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['mod{}_opros'.format(i + 1)]['fg'] = 'green'
                    elif ansvers[i][18:22] == '0000':
                        globals()['work{}_opros'.format(i + 1)]['text'] = 'Откл'
                        globals()['work{}_opros'.format(i + 1)]['fg'] = 'blue'
                        globals()['pitan{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['pitan{}_opros'.format(i + 1)]['fg'] = 'green'
                        globals()['mod{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['mod{}_opros'.format(i + 1)]['fg'] = 'green'
                    else:
                        avaria_47(ansvers[i][18:22], i)
                if ansvers[i][6:8] == '49':
                    if ansvers[i][18:22] == '0007' and ansvers[i][36:40] == '0007':
                        globals()['work{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['work{}_opros'.format(i + 1)]['fg'] = 'green'
                        globals()['pitan{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['pitan{}_opros'.format(i + 1)]['fg'] = 'green'
                        globals()['mod{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['mod{}_opros'.format(i + 1)]['fg'] = 'green'
                    elif ansvers[i][18:22] == '0000' and ansvers[i][36:40] == '0000':
                        globals()['work{}_opros'.format(i + 1)]['text'] = 'Откл'
                        globals()['work{}_opros'.format(i + 1)]['fg'] = 'blue'
                        globals()['pitan{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['pitan{}_opros'.format(i + 1)]['fg'] = 'green'
                        globals()['mod{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['mod{}_opros'.format(i + 1)]['fg'] = 'green'
                    else:
                        avaria_49(ansvers[i][18:22], ansvers[i][36:40], i)
                if ansvers[i][6:8] == '51':
                    if ansvers[i][36:40] == '0007' and ansvers[i][54:58] == '0000' and ansvers[i][72:76] == '0000' \
                                                                                   and ansvers[i][90:94] == '0000':
                        globals()['work{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['work{}_opros'.format(i + 1)]['fg'] = 'green'
                        globals()['pitan{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['pitan{}_opros'.format(i + 1)]['fg'] = 'green'
                        globals()['mod{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['mod{}_opros'.format(i + 1)]['fg'] = 'green'
                    elif ansvers[i][36:40] == '0000':
                        globals()['work{}_opros'.format(i + 1)]['text'] = 'Откл'
                        globals()['work{}_opros'.format(i + 1)]['fg'] = 'blue'
                        globals()['pitan{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['pitan{}_opros'.format(i + 1)]['fg'] = 'green'
                        globals()['mod{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['mod{}_opros'.format(i + 1)]['fg'] = 'green'
                    else:
                        avaria_51(ansvers[i][36:40], ansvers[i][54:58], ansvers[i][72:76], ansvers[i][90:94], i)
        time.sleep(0.1)


def stop_obmen():
    opros.flag_on_opros = not opros.flag_on_opros


def choise_active_module(b):
    opros.active_module[b] = not opros.active_module[b]


def vkl_pitan():
    opros.active_parametrs[0] = not opros.active_parametrs[0]


def vkl_ip():
    opros.active_parametrs[1] = not opros.active_parametrs[1]


def vkl_svch():
    opros.active_parametrs[2] = not opros.active_parametrs[2]


def vkl_vikl_active_module():
    global number_of_modules
    global flag_vkl_vikl_active_module
    flag_vkl_vikl_active_module = not flag_vkl_vikl_active_module
    if flag_vkl_vikl_active_module is True:
        button_vkl_vikl['text'] = 'ВКЛ'
        button_vkl_vikl['bg'] = 'green yellow'
        for i in range(number_of_modules):
            if opros.active_module[i] is True:
                if opros.active_parametrs[0] is True:
                    opros.list_modules_command_vkl[i] = opros.list_modules_command_vkl[i][0] + '1' + \
                                                        opros.list_modules_command_vkl[i][2:]
                else:
                    opros.list_modules_command_vkl[i] = opros.list_modules_command_vkl[i][0] + '0' + \
                                                        opros.list_modules_command_vkl[i][2:]
                if opros.active_parametrs[1] is True:
                    opros.list_modules_command_vkl[i] = opros.list_modules_command_vkl[i][0:3] + '1' + \
                                                        opros.list_modules_command_vkl[i][4:]
                else:
                    opros.list_modules_command_vkl[i] = opros.list_modules_command_vkl[i][0:3] + '0' + \
                                                        opros.list_modules_command_vkl[i][4:]
                if opros.active_parametrs[2] is True:
                    opros.list_modules_command_vkl[i] = opros.list_modules_command_vkl[i][0:5] + '1' + \
                                                        opros.list_modules_command_vkl[i][6:]
                else:
                    opros.list_modules_command_vkl[i] = opros.list_modules_command_vkl[i][0:5] + '0' + \
                                                        opros.list_modules_command_vkl[i][6:]
    else:
        button_vkl_vikl['text'] = 'ВЫКЛ'
        button_vkl_vikl['bg'] = 'snow3'
        for i in range(number_of_modules):
            if opros.active_module[i] is True:
                opros.list_modules_command_vkl[i] = opros.list_modules_command_vkl[i][0] + '0' + \
                                                    opros.list_modules_command_vkl[i][2:]
                opros.list_modules_command_vkl[i] = opros.list_modules_command_vkl[i][0:3] + '0' + \
                                                    opros.list_modules_command_vkl[i][4:]
                opros.list_modules_command_vkl[i] = opros.list_modules_command_vkl[i][0:5] + '0' + \
                                                    opros.list_modules_command_vkl[i][6:]


def avaria_47(ks, i):  # приём в качестве аргумента 4 байта контрольного слова
    ksb1 = list(bin(int(ks[:2], 16))[2:])  # превращение НЕХ значений в BIN значения
    ksb2 = list(bin(int(ks[2:], 16))[2:])  # превращение НЕХ значений в BIN значения
    ksb1 = ['0' for i in range(8 - len(ksb1))] + ksb1  # превращение BIN значений в массив из 8 битов
    ksb2 = ['0' for i in range(8 - len(ksb2))] + ksb2  # превращение BIN значений в массив из 8 битов
    if ksb1[-1] == '1' or ksb1[-2] == '1' or ksb1[-3] == '1':
        globals()['work{}_opros'.format(i + 1)]['text'] = 'Авария'
        globals()['work{}_opros'.format(i + 1)]['fg'] = 'red'
        if ksb1[-1] == '1':
            globals()['mod{}_opros'.format(i + 1)]['text'] = 'перегрузка по T/Q'
            globals()['mod{}_opros'.format(i + 1)]['fg'] = 'red'
        else:
            if ksb1[-2] == '1':
                globals()['mod{}_opros'.format(i + 1)]['text'] = 'Нет ИМ'
                globals()['mod{}_opros'.format(i + 1)]['fg'] = 'red'
            else:
                globals()['mod{}_opros'.format(i + 1)]['text'] = 'Норма'
                globals()['mod{}_opros'.format(i + 1)]['fg'] = 'green'
        if ksb1[-3] == '1':
            globals()['pitan{}_opros'.format(i + 1)]['text'] = 'Авария'
            globals()['pitan{}_opros'.format(i + 1)]['fg'] = 'red'
        else:
            globals()['pitan{}_opros'.format(i + 1)]['text'] = 'Норма'
            globals()['pitan{}_opros'.format(i + 1)]['fg'] = 'green'
    else:
        globals()['pitan{}_opros'.format(i + 1)]['text'] = 'Норма'
        globals()['pitan{}_opros'.format(i + 1)]['fg'] = 'green'
        globals()['mod{}_opros'.format(i + 1)]['text'] = 'Норма'
        globals()['mod{}_opros'.format(i + 1)]['fg'] = 'green'
        if ksb2[-4] == '1':
            globals()['work{}_opros'.format(i + 1)]['text'] = 'Рвх меньше\nнормы'
            globals()['work{}_opros'.format(i + 1)]['fg'] = 'orange'
        elif ksb2[-5] == '1':
            globals()['work{}_opros'.format(i + 1)]['text'] = 'Рвх больше\nнормы'
            globals()['work{}_opros'.format(i + 1)]['fg'] = 'orange'
        elif ksb2[-6] == '1':
            globals()['work{}_opros'.format(i + 1)]['text'] = 'Рвых меньше\nнормы'
            globals()['work{}_opros'.format(i + 1)]['fg'] = 'orange'
        elif ksb2[-7] == '1':
            globals()['work{}_opros'.format(i + 1)]['text'] = 'Ротр больше\nнормы'
            globals()['work{}_opros'.format(i + 1)]['fg'] = 'orange'
        elif ksb2[-8] == '1':
            globals()['work{}_opros'.format(i + 1)]['text'] = 'Перегрев'
            globals()['work{}_opros'.format(i + 1)]['fg'] = 'orange'
        elif ksb1[-4] == '1':
            globals()['work{}_opros'.format(i + 1)]['text'] = 'Датчик темп.\nнеисправен'
            globals()['work{}_opros'.format(i + 1)]['fg'] = 'orange'


def avaria_49(ks1, ks2, i):
    ks1b1 = list(bin(int(ks1[:2], 16))[2:])  # превращение НЕХ значений в BIN значения
    ks1b2 = list(bin(int(ks1[2:], 16))[2:])  # превращение НЕХ значений в BIN значения
    ks2b1 = list(bin(int(ks2[:2], 16))[2:])  # превращение НЕХ значений в BIN значения
    ks2b2 = list(bin(int(ks2[2:], 16))[2:])  # превращение НЕХ значений в BIN значения
    ks1b1 = ['0' for i in range(8 - len(ks1b1))] + ks1b1  # превращение BIN значений в массив из 8 битов
    ks1b2 = ['0' for i in range(8 - len(ks1b2))] + ks1b2  # превращение BIN значений в массив из 8 битов
    ks2b1 = ['0' for i in range(8 - len(ks2b1))] + ks2b1  # превращение BIN значений в массив из 8 битов
    ks2b2 = ['0' for i in range(8 - len(ks2b2))] + ks2b2  # превращение BIN значений в массив из 8 битов
    if ks1b1[-1] == '1' or ks1b1[-2] == '1' or ks1b1[-3] == '1' or \
            ks2b1[-1] == '1' or ks2b1[-2] == '1' or ks2b1[-3] == '1':
        globals()['work{}_opros'.format(i + 1)]['text'] = 'Авария'
        globals()['work{}_opros'.format(i + 1)]['fg'] = 'red'
        if ks1b1[-1] == '1' or ks2b1[-1] == '1':
            globals()['mod{}_opros'.format(i + 1)]['text'] = 'перегрузка\nпо T/Q'
            globals()['mod{}_opros'.format(i + 1)]['fg'] = 'red'
        else:
            if ks1b1[-2] == '1' or ks2b1[-2] == '1':
                globals()['mod{}_opros'.format(i + 1)]['text'] = 'Нет ИМ'
                globals()['mod{}_opros'.format(i + 1)]['fg'] = 'red'
            else:
                globals()['mod{}_opros'.format(i + 1)]['text'] = 'Норма'
                globals()['mod{}_opros'.format(i + 1)]['fg'] = 'green'
        if ks1b1[-3] == '1' or ks2b1[-3] == '1':
            globals()['pitan{}_opros'.format(i + 1)]['text'] = 'Авария'
            globals()['pitan{}_opros'.format(i + 1)]['fg'] = 'red'
        else:
            globals()['pitan{}_opros'.format(i + 1)]['text'] = 'Норма'
            globals()['pitan{}_opros'.format(i + 1)]['fg'] = 'green'
    else:
        globals()['pitan{}_opros'.format(i + 1)]['text'] = 'Норма'
        globals()['pitan{}_opros'.format(i + 1)]['fg'] = 'green'
        globals()['mod{}_opros'.format(i + 1)]['text'] = 'Норма'
        globals()['mod{}_opros'.format(i + 1)]['fg'] = 'green'
        if ks1b2[-4] == '1' or ks2b2[-4] == '1':
            globals()['work{}_opros'.format(i + 1)]['text'] = 'Рвх меньше\nнормы'
            globals()['work{}_opros'.format(i + 1)]['fg'] = 'orange'
        elif ks1b2[-5] == '1' or ks2b2[-5] == '1':
            globals()['work{}_opros'.format(i + 1)]['text'] = 'Рвх больше\nнормы'
            globals()['work{}_opros'.format(i + 1)]['fg'] = 'orange'
        elif ks1b2[-6] == '1' or ks2b2[-6] == '1':
            globals()['work{}_opros'.format(i + 1)]['text'] = 'Рвых меньше\nнормы'
            globals()['work{}_opros'.format(i + 1)]['fg'] = 'orange'
        elif ks1b2[-7] == '1' or ks2b2[-7] == '1':
            globals()['work{}_opros'.format(i + 1)]['text'] = 'Ротр больше\nнормы'
            globals()['work{}_opros'.format(i + 1)]['fg'] = 'orange'
        elif ks1b2[-8] == '1' or ks2b2[-8] == '1':
            globals()['work{}_opros'.format(i + 1)]['text'] = 'Перегрев'
            globals()['work{}_opros'.format(i + 1)]['fg'] = 'orange'
        elif ks1b1[-4] == '1' or ks2b1[-4] == '1':
            globals()['work{}_opros'.format(i + 1)]['text'] = 'Датчик темп.\nнеисправен'
            globals()['work{}_opros'.format(i + 1)]['fg'] = 'orange'


def avaria_51(ks1, ks2, ks3, ks4, i):
    ks1b1 = list(bin(int(ks1[:2], 16))[2:])  # превращение НЕХ значений в BIN значения
    ks1b2 = list(bin(int(ks1[2:], 16))[2:])  # превращение НЕХ значений в BIN значения
    ks2b1 = list(bin(int(ks2[:2], 16))[2:])  # превращение НЕХ значений в BIN значения
    ks2b2 = list(bin(int(ks2[2:], 16))[2:])  # превращение НЕХ значений в BIN значения
    ks3b1 = list(bin(int(ks3[:2], 16))[2:])  # превращение НЕХ значений в BIN значения
    ks3b2 = list(bin(int(ks3[2:], 16))[2:])  # превращение НЕХ значений в BIN значения
    ks4b1 = list(bin(int(ks4[:2], 16))[2:])  # превращение НЕХ значений в BIN значения
    ks4b2 = list(bin(int(ks4[2:], 16))[2:])  # превращение НЕХ значений в BIN значения
    ks1b1 = ['0' for i in range(8 - len(ks1b1))] + ks1b1  # превращение BIN значений в массив из 8 битов
    ks1b2 = ['0' for i in range(8 - len(ks1b2))] + ks1b2  # превращение BIN значений в массив из 8 битов
    ks2b1 = ['0' for i in range(8 - len(ks2b1))] + ks2b1  # превращение BIN значений в массив из 8 битов
    ks2b2 = ['0' for i in range(8 - len(ks2b2))] + ks2b2  # превращение BIN значений в массив из 8 битов
    ks3b1 = ['0' for i in range(8 - len(ks3b1))] + ks1b1  # превращение BIN значений в массив из 8 битов
    ks3b2 = ['0' for i in range(8 - len(ks3b2))] + ks1b2  # превращение BIN значений в массив из 8 битов
    ks4b1 = ['0' for i in range(8 - len(ks4b1))] + ks2b1  # превращение BIN значений в массив из 8 битов
    ks4b2 = ['0' for i in range(8 - len(ks4b2))] + ks2b2  # превращение BIN значений в массив из 8 битов
    if ks1b1[-1] == '1' or ks1b1[-2] == '1' or ks1b1[-3] == '1' or \
            ks2b1[-1] == '1' or ks2b1[-2] == '1' or ks2b1[-3] == '1':
        globals()['work{}_opros'.format(i + 1)]['text'] = 'Авария'
        globals()['work{}_opros'.format(i + 1)]['fg'] = 'red'
        if ks1b1[-1] == '1' or ks2b1[-1] == '1':
            globals()['mod{}_opros'.format(i + 1)]['text'] = 'перегрузка\nпо T/Q'
            globals()['mod{}_opros'.format(i + 1)]['fg'] = 'red'
        else:
            if ks1b1[-2] == '1' or ks2b1[-2] == '1':
                globals()['mod{}_opros'.format(i + 1)]['text'] = 'Нет ИМ'
                globals()['mod{}_opros'.format(i + 1)]['fg'] = 'red'
            else:
                globals()['mod{}_opros'.format(i + 1)]['text'] = 'Норма'
                globals()['mod{}_opros'.format(i + 1)]['fg'] = 'green'
        if ks1b1[-3] == '1' or ks2b1[-3] == '1':
            globals()['pitan{}_opros'.format(i + 1)]['text'] = 'Авария'
            globals()['pitan{}_opros'.format(i + 1)]['fg'] = 'red'
        else:
            globals()['pitan{}_opros'.format(i + 1)]['text'] = 'Норма'
            globals()['pitan{}_opros'.format(i + 1)]['fg'] = 'green'
    else:
        globals()['pitan{}_opros'.format(i + 1)]['text'] = 'Норма'
        globals()['pitan{}_opros'.format(i + 1)]['fg'] = 'green'
        globals()['mod{}_opros'.format(i + 1)]['text'] = 'Норма'
        globals()['mod{}_opros'.format(i + 1)]['fg'] = 'green'
        if ks1b2[-4] == '1' or ks2b2[-4] == '1':
            globals()['work{}_opros'.format(i + 1)]['text'] = 'Рвх меньше\nнормы'
            globals()['work{}_opros'.format(i + 1)]['fg'] = 'orange'
        elif ks1b2[-5] == '1' or ks2b2[-5] == '1':
            globals()['work{}_opros'.format(i + 1)]['text'] = 'Рвх больше\nнормы'
            globals()['work{}_opros'.format(i + 1)]['fg'] = 'orange'
        elif ks1b2[-6] == '1' or ks2b2[-6] == '1':
            globals()['work{}_opros'.format(i + 1)]['text'] = 'Рвых меньше\nнормы'
            globals()['work{}_opros'.format(i + 1)]['fg'] = 'orange'
        elif ks1b2[-7] == '1' or ks2b2[-7] == '1':
            globals()['work{}_opros'.format(i + 1)]['text'] = 'Ротр больше\nнормы'
            globals()['work{}_opros'.format(i + 1)]['fg'] = 'orange'
        elif ks1b2[-8] == '1' or ks2b2[-8] == '1':
            globals()['work{}_opros'.format(i + 1)]['text'] = 'Перегрев'
            globals()['work{}_opros'.format(i + 1)]['fg'] = 'orange'
        elif ks1b1[-4] == '1' or ks2b1[-4] == '1':
            globals()['work{}_opros'.format(i + 1)]['text'] = 'Датчик темп.\nнеисправен'
            globals()['work{}_opros'.format(i + 1)]['fg'] = 'orange'


def sbros_avarii():
    opros.flag_sbros_avrii = True


thread_opros = threading.Thread(target=opros.obmen, daemon=True)
thread_update_window = threading.Thread(target=update_window, daemon=True)

'''Создание окна'''
window = tkinter.Tk()
window.title("Универсальная программа")

for i in range(0, number_of_modules):
    locals()['module{}'.format(i+1)] = tkinter.Label(window, text='модуль {}'.format(i+1))
for i in range(0, number_of_modules):
    locals()['button{}'.format(i+1)] = tkinter.Button(window, text='параметры',
                                                      command=lambda type_window=opros.list_command[i],
                                                      how_module=i:
                                                      param_module.full_information_of_module(type_window, how_module))
for i in range(0, number_of_modules):
    globals()['check{}'.format(i+1)] = tkinter.Checkbutton(window,
                                                           command=lambda b=i: choise_active_module(b))
for i in range(0, number_of_modules):

    locals()['work{}'.format(i+1)] = tkinter.Label(window, text='Работа:')
for i in range(0, number_of_modules):
    globals()['work{}_opros'.format(i+1)] = tkinter.Label(window, text='0_о', fg='red')

for i in range(0, number_of_modules):
    locals()['pitan{}'.format(i+1)] = tkinter.Label(window, text='Питание:')
for i in range(0, number_of_modules):
    globals()['pitan{}_opros'.format(i+1)] = tkinter.Label(window, text='0_о', fg='red')

for i in range(0, number_of_modules):
    locals()['mod{}'.format(i+1)] = tkinter.Label(window, text='Модуляция:')
for i in range(0, number_of_modules):
    globals()['mod{}_opros'.format(i+1)] = tkinter.Label(window, text='0_о', fg='red')

button_vkl_vikl = tkinter.Button(window, text='ВЫКЛ', width=10, heigh=2, font='arial 15', bg='snow3',
                                 command=vkl_vikl_active_module)
sbros = tkinter.Button(window, text='Сброс\nаварии', width=10, heigh=2, font='arial 15', bg='snow3',
                       command=sbros_avarii)

vkl_vikl_pitan = tkinter.Checkbutton(window, command=vkl_pitan)
vkl_vikl_ip = tkinter.Checkbutton(window, command=vkl_ip)
vkl_vikl_svch = tkinter.Checkbutton(window, command=vkl_svch)
chooise_all = tkinter.Checkbutton(window, text='выбрать все\nмодули', command=all_vum_use)
stop_obmen = tkinter.Checkbutton(window, text='стоп обмен', command=stop_obmen)

vkl_vikl_pitan_label = tkinter.Label(window, text='Сеть')
vkl_vikl_ip_label = tkinter.Label(window, text='ИП')
vkl_vikl_svch_label = tkinter.Label(window, text='СВЧ')

vkl_vikl_svch.select()
vkl_vikl_ip.select()
vkl_vikl_pitan.select()

for i in range(1, number_of_modules+1):
    locals()['module{}'.format(i)].place(x=50, y=35*(i-1)+10)
for i in range(1, number_of_modules+1):
    locals()['button{}'.format(i)].place(x=150, y=35*(i-1)+10)
for i in range(1, number_of_modules+1):
    locals()['check{}'.format(i)].place(x=120, y=35*(i-1)+10)

for i in range(1, number_of_modules+1):
    locals()['work{}'.format(i)].place(x=250, y=35*(i-1)+10)
for i in range(1, number_of_modules+1):
    locals()['work{}_opros'.format(i)].place(x=295, y=35*(i-1)+10)

for i in range(1, number_of_modules+1):
    locals()['pitan{}'.format(i)].place(x=380, y=35*(i-1)+10)
for i in range(1, number_of_modules+1):
    locals()['pitan{}_opros'.format(i)].place(x=435, y=35*(i-1)+10)

for i in range(1, number_of_modules+1):
    locals()['mod{}'.format(i)].place(x=500, y=35*(i-1)+10)
for i in range(1, number_of_modules+1):
    locals()['mod{}_opros'.format(i)].place(x=570, y=35*(i-1)+10)


button_vkl_vikl.place(x=50, y=35*number_of_modules+20)
sbros.place(x=200, y=35*number_of_modules+20)
vkl_vikl_pitan.place(x=60, y=35*number_of_modules+110)
vkl_vikl_ip.place(x=100, y=35*number_of_modules+110)
vkl_vikl_svch.place(x=140, y=35*number_of_modules+110)
vkl_vikl_pitan_label.place(x=60, y=35*number_of_modules+90)
vkl_vikl_ip_label.place(x=100, y=35*number_of_modules+90)
vkl_vikl_svch_label.place(x=140, y=35*number_of_modules+90)
chooise_all.place(x=200, y=35*number_of_modules+90)
stop_obmen.place(x=400, y=35*number_of_modules+90)

thread_update_window.start()
thread_opros.start()

window.geometry(str(650) + 'x' + str(35*(number_of_modules + 1) + 120) + '+300+10')

window.mainloop()
