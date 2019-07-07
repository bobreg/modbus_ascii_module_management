import tkinter
import opros
import param_module
import time
import threading
import start

general_shift = 50 # переменная для сдвига всех элементов по вертикали

flag_cheks = True  # флаг для того чтобы ставить и снимать галочки на всех модулях
flag_cheks_on_51 = True  # флаг для того чтобы ставить и снимать галочки на всех модулях при активации 51 команды
flag_vkl_vikl_active_module = False


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


def all_vum_on_51():
    global flag_cheks_on_51
    if flag_cheks_on_51 is True:
        for j in range(1, number_of_modules + 1):
            globals()['check_51{}'.format(j)].select()
            if opros.list_command[j-1] == '47':
                opros.list_command[j-1] = '51'
                opros.list_modules_command_vkl[j-1] = '00000002'
            elif opros.list_command[j-1] == '49':
                opros.list_command[j-1] = '51'
                opros.list_modules_command_vkl[j-1] = '00000003'
    else:
        for j in range(1, number_of_modules + 1):
            globals()['check_51{}'.format(j)].deselect()
            opros.list_command[j-1] = opros.list_command_buffer[j-1]
            opros.list_modules_command_vkl[j-1] = opros.list_modules_command_vkl_buffer[j-1]
    flag_cheks_on_51 = not flag_cheks_on_51


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
                    elif int(ansvers[i][18:22], 16) < 7:
                        globals()['work{}_opros'.format(i + 1)]['text'] = 'Откл'
                        globals()['work{}_opros'.format(i + 1)]['fg'] = 'blue'
                        globals()['pitan{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['pitan{}_opros'.format(i + 1)]['fg'] = 'green'
                        globals()['mod{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['mod{}_opros'.format(i + 1)]['fg'] = 'green'
                    else:
                        avaria_47(ansvers[i][18:22], i)
                elif ansvers[i][6:8] == '49':
                    if ansvers[i][18:22] == '0007' and ansvers[i][36:40] == '0007':
                        globals()['work{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['work{}_opros'.format(i + 1)]['fg'] = 'green'
                        globals()['pitan{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['pitan{}_opros'.format(i + 1)]['fg'] = 'green'
                        globals()['mod{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['mod{}_opros'.format(i + 1)]['fg'] = 'green'
                    elif int(ansvers[i][18:22], 16) < 7 and int(ansvers[i][36:40], 16) < 7:
                        globals()['work{}_opros'.format(i + 1)]['text'] = 'Откл'
                        globals()['work{}_opros'.format(i + 1)]['fg'] = 'blue'
                        globals()['pitan{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['pitan{}_opros'.format(i + 1)]['fg'] = 'green'
                        globals()['mod{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['mod{}_opros'.format(i + 1)]['fg'] = 'green'
                    else:
                        avaria_49(ansvers[i][18:22], ansvers[i][36:40], i)
                elif ansvers[i][6:8] == '51' and ansvers[i][8:10] == '02':
                    if ansvers[i][36:40] == '0007':
                        globals()['work{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['work{}_opros'.format(i + 1)]['fg'] = 'green'
                        globals()['pitan{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['pitan{}_opros'.format(i + 1)]['fg'] = 'green'
                        globals()['mod{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['mod{}_opros'.format(i + 1)]['fg'] = 'green'
                    elif int(ansvers[i][36:40], 16) < 7:
                        globals()['work{}_opros'.format(i + 1)]['text'] = 'Откл'
                        globals()['work{}_opros'.format(i + 1)]['fg'] = 'blue'
                        globals()['pitan{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['pitan{}_opros'.format(i + 1)]['fg'] = 'green'
                        globals()['mod{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['mod{}_opros'.format(i + 1)]['fg'] = 'green'
                    else:
                        avaria_51(ansvers[i][36:40], '0000', '0000', '0000', i)
                elif ansvers[i][6:8] == '51' and ansvers[i][8:10] == '03':
                    if ansvers[i][36:40] == '0007' and ansvers[i][54:58] == '0000':
                        globals()['work{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['work{}_opros'.format(i + 1)]['fg'] = 'green'
                        globals()['pitan{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['pitan{}_opros'.format(i + 1)]['fg'] = 'green'
                        globals()['mod{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['mod{}_opros'.format(i + 1)]['fg'] = 'green'
                    elif int(ansvers[i][36:40], 16) < 7:
                        globals()['work{}_opros'.format(i + 1)]['text'] = 'Откл'
                        globals()['work{}_opros'.format(i + 1)]['fg'] = 'blue'
                        globals()['pitan{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['pitan{}_opros'.format(i + 1)]['fg'] = 'green'
                        globals()['mod{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['mod{}_opros'.format(i + 1)]['fg'] = 'green'
                    else:
                        avaria_51(ansvers[i][36:40], ansvers[i][54:58], '0000', '0000', i)
                elif ansvers[i][6:8] == '51' and ansvers[i][8:10] == '05':
                    if ansvers[i][36:40] == '0007' and ansvers[i][54:58] == '0000' and ansvers[i][72:76] == '0000' \
                                                                                   and ansvers[i][90:94] == '0000':
                        globals()['work{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['work{}_opros'.format(i + 1)]['fg'] = 'green'
                        globals()['pitan{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['pitan{}_opros'.format(i + 1)]['fg'] = 'green'
                        globals()['mod{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['mod{}_opros'.format(i + 1)]['fg'] = 'green'
                    elif int(ansvers[i][36:40], 16) < 7:
                        globals()['work{}_opros'.format(i + 1)]['text'] = 'Откл'
                        globals()['work{}_opros'.format(i + 1)]['fg'] = 'blue'
                        globals()['pitan{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['pitan{}_opros'.format(i + 1)]['fg'] = 'green'
                        globals()['mod{}_opros'.format(i + 1)]['text'] = 'норм'
                        globals()['mod{}_opros'.format(i + 1)]['fg'] = 'green'
                    else:
                        avaria_51(ansvers[i][36:40], ansvers[i][54:58], ansvers[i][72:76], ansvers[i][90:94], i)
                else:
                    globals()['work{}_opros'.format(i + 1)]['fg'] = 'orange'
                    globals()['work{}_opros'.format(i + 1)]['text'] = 'аномалия'
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
        button_vkl_vikl['text'] = 'ВЫКЛ'
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
        button_vkl_vikl['text'] = 'ВКЛ'
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


def sent_51_in_module(s):
    if opros.list_command[s] == '47':
        opros.list_command[s] = '51'
        opros.list_modules_command_vkl[s] = '00000002'
    elif opros.list_command[s] == '49':
        opros.list_command[s] = '51'
        opros.list_modules_command_vkl[s] = '00000003'
    elif opros.list_command[s] == '51':
        opros.list_command[s] = opros.list_command_buffer[s]
        opros.list_modules_command_vkl[s] = opros.list_modules_command_vkl_buffer[s]


def scroll_def(event):
    canvas.configure(scrollregion=canvas.bbox('all'))


thread_opros = threading.Thread(target=opros.obmen, daemon=True)
thread_update_window = threading.Thread(target=update_window, daemon=True)

'''Создание окна'''
window = tkinter.Tk()
window.title("Универсальная программа")

if number_of_modules <= 16:
    window.geometry(str(760) + 'x' + str(35 * (number_of_modules + 1) + 150) + '+300+0')
    canvas = tkinter.Canvas(window, width=750, height=35*(number_of_modules + 1) + 150)
    frame_for_elements = tkinter.Frame(canvas, width=750, height=35 * (number_of_modules + 1) + 150)
    frame_for_elements.place(x=0, y=0)
else:
    window.geometry(str(760) + 'x' + str(730) + '+300+0')
    canvas = tkinter.Canvas(window, width=750, height=730, bg='green')
    frame_for_elements = tkinter.Frame(canvas, width=750, height=35 * (number_of_modules + 1) + 150)
    scroll = tkinter.Scrollbar(window, command=canvas.yview)
    canvas['yscrollcommand'] = scroll.set
    scroll.pack(side='right', fill='y')
    canvas.create_window((0, 0), window=frame_for_elements, anchor='nw')
    window.bind('<Configure>', scroll_def)




adress_label = tkinter.Label(frame_for_elements, text='Адрес\nмодуля', font='Gothice 8')
activate_control_label = tkinter.Label(frame_for_elements, text='Активировать\nуправление', font='Gothice 8')
general_state_label = tkinter.Label(frame_for_elements, text='Общее состояние модулей', font='Gothice 14')
on_51_in_modules = tkinter.Label(frame_for_elements, text='Опрашивать\n51 командой', font='Gothice 8')
c1 = tkinter.Canvas(frame_for_elements, width=2, height=35*number_of_modules+25, bg='snow3')
c2 = tkinter.Canvas(frame_for_elements, width=2, height=35*number_of_modules+25, bg='snow3')
c3 = tkinter.Canvas(frame_for_elements, width=2, height=35*number_of_modules+25, bg='snow3')

for i in range(0, number_of_modules):
    locals()['adress_module{}'.format(i+1)] = tkinter.Label(frame_for_elements, text='{}'.format(opros.list_modules[i]))
for i in range(0, number_of_modules):
    locals()['module{}'.format(i+1)] = tkinter.Label(frame_for_elements, text='модуль {}'.format(i+1))
for i in range(0, number_of_modules):
    locals()['button{}'.format(i+1)] = tkinter.Button(frame_for_elements, text='параметры',
                                                      command=lambda type_window=opros.list_command[i],
                                                      how_module=i:
                                                      param_module.full_information_of_module(type_window, how_module))
for i in range(0, number_of_modules):
    globals()['check{}'.format(i+1)] = tkinter.Checkbutton(frame_for_elements,
                                                           command=lambda b=i: choise_active_module(b))
for i in range(0, number_of_modules):
    globals()['check_51{}'.format(i+1)] = tkinter.Checkbutton(frame_for_elements,
                                                           command=lambda s=i: sent_51_in_module(s))
for i in range(0, number_of_modules):
    locals()['work{}'.format(i+1)] = tkinter.Label(frame_for_elements, text='Работа:')
for i in range(0, number_of_modules):
    globals()['work{}_opros'.format(i+1)] = tkinter.Label(frame_for_elements, text='0_о', fg='red')

for i in range(0, number_of_modules):
    locals()['pitan{}'.format(i+1)] = tkinter.Label(frame_for_elements, text='Питание:')
for i in range(0, number_of_modules):
    globals()['pitan{}_opros'.format(i+1)] = tkinter.Label(frame_for_elements, text='0_о', fg='red')

for i in range(0, number_of_modules):
    locals()['mod{}'.format(i+1)] = tkinter.Label(frame_for_elements, text='Модуляция:')
for i in range(0, number_of_modules):
    globals()['mod{}_opros'.format(i+1)] = tkinter.Label(frame_for_elements, text='0_о', fg='red')

button_vkl_vikl = tkinter.Button(frame_for_elements, text='ВКЛ', width=10, heigh=2, font='arial 15', bg='snow3',
                                 command=vkl_vikl_active_module)
sbros = tkinter.Button(frame_for_elements, text='Сброс\nаварии', width=10, heigh=2, font='arial 15', bg='snow3',
                       command=sbros_avarii)

vkl_vikl_pitan = tkinter.Checkbutton(frame_for_elements, command=vkl_pitan)
vkl_vikl_ip = tkinter.Checkbutton(frame_for_elements, command=vkl_ip)
vkl_vikl_svch = tkinter.Checkbutton(frame_for_elements, command=vkl_svch)
chooise_all = tkinter.Checkbutton(frame_for_elements, text='выбрать все\nмодули', command=all_vum_use)
stop_obmen = tkinter.Checkbutton(frame_for_elements, text='стоп обмен', command=stop_obmen)
chooise_all_on_51 = tkinter.Checkbutton(frame_for_elements, text='все', command=all_vum_on_51)

vkl_vikl_pitan_label = tkinter.Label(frame_for_elements, text='Сеть')
vkl_vikl_ip_label = tkinter.Label(frame_for_elements, text='ИП')
vkl_vikl_svch_label = tkinter.Label(frame_for_elements, text='СВЧ')

vkl_vikl_svch.select()
vkl_vikl_ip.select()
vkl_vikl_pitan.select()

'''размещение элементов'''

canvas.place(x=0, y=0)


adress_label.place(x=5, y=5)
activate_control_label.place(x=140, y=5)
general_state_label.place(x=300, y=5)
on_51_in_modules.place(x=655, y=5)
c1.place(x=115, y=10)
c2.place(x=250, y=10)
c3.place(x=640, y=10)

for i in range(1, number_of_modules+1):
    locals()['adress_module{}'.format(i)].place(x=15, y=35*(i-1)+general_shift)
for i in range(1, number_of_modules+1):
    locals()['module{}'.format(i)].place(x=50, y=35*(i-1)+general_shift)
for i in range(1, number_of_modules+1):
    locals()['button{}'.format(i)].place(x=160, y=35*(i-1)+general_shift)
for i in range(1, number_of_modules+1):
    locals()['check{}'.format(i)].place(x=130, y=35*(i-1)+general_shift)
for i in range(1, number_of_modules+1):
    locals()['check_51{}'.format(i)].place(x=680, y=35*(i-1)+general_shift)

for i in range(1, number_of_modules+1):
    locals()['work{}'.format(i)].place(x=270, y=35*(i-1)+general_shift)
for i in range(1, number_of_modules+1):
    locals()['work{}_opros'.format(i)].place(x=315, y=35*(i-1)+general_shift)

for i in range(1, number_of_modules+1):
    locals()['pitan{}'.format(i)].place(x=400, y=35*(i-1)+general_shift)
for i in range(1, number_of_modules+1):
    locals()['pitan{}_opros'.format(i)].place(x=455, y=35*(i-1)+general_shift)

for i in range(1, number_of_modules+1):
    locals()['mod{}'.format(i)].place(x=520, y=35*(i-1)+general_shift)
for i in range(1, number_of_modules+1):
    locals()['mod{}_opros'.format(i)].place(x=590, y=35*(i-1)+general_shift)


button_vkl_vikl.place(x=50, y=35*number_of_modules+general_shift)
sbros.place(x=200, y=35*number_of_modules+general_shift)
vkl_vikl_pitan.place(x=60, y=35*number_of_modules+100+general_shift)
vkl_vikl_ip.place(x=100, y=35*number_of_modules+100+general_shift)
vkl_vikl_svch.place(x=140, y=35*number_of_modules+100+general_shift)
vkl_vikl_pitan_label.place(x=60, y=35*number_of_modules+80+general_shift)
vkl_vikl_ip_label.place(x=100, y=35*number_of_modules+80+general_shift)
vkl_vikl_svch_label.place(x=140, y=35*number_of_modules+80+general_shift)
chooise_all.place(x=200, y=35*number_of_modules+80+general_shift)
stop_obmen.place(x=400, y=35*number_of_modules+80+general_shift)
chooise_all_on_51.place(x=680, y=35*number_of_modules+general_shift)

thread_update_window.start()
thread_opros.start()

window.mainloop()
