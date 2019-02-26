import tkinter
import threading
import opros
import time


def full_information_of_module(type_window, how_module):
    if type_window == '47':
        window47(how_module)
    if type_window == '49':
        window49(how_module)
    if type_window == '51':
        window51(how_module)


def window47(how_module):
    global P_mirrow
    window_47 = tkinter.Tk()
    window_47.title('Параметры {} модуля'.format(how_module+1))
    window_47.geometry('250x400')

    param_label = tkinter.Label(window_47, justify='right', text='Серийный номер:\n\n'
                                                                 'Версия прошивки:\n\n'
                                                                 'Время работы, ч:\n\n'
                                                                 'Время работы, мин:\n\n'
                                                                 'Температура, ºC:\n\n'
                                                                 'Напряжение питания, В:\n\n'
                                                                 'Контрольное слово:\n\n'
                                                                 'Входная мощность, у.е.:\n\n'
                                                                 'Выходная мощность, у.е.:\n\n'
                                                                 'Отражённая мощность, у.е.:\n\n'
                                                                 'Текущий код фазы:\n\n'
                                                                 'Заводской код фазы:')

    globals()['s_number{}'.format(how_module)] = tkinter.Label(window_47, text='FF')
    globals()['version_p{}'.format(how_module)] = tkinter.Label(window_47, text='FF')
    globals()['time_work{}'.format(how_module)] = tkinter.Label(window_47, text='FF')
    globals()['temperature{}'.format(how_module)] = tkinter.Label(window_47, text='FF')
    globals()['time_work_min{}'.format(how_module)] = tkinter.Label(window_47, text='FF')
    globals()['voltage{}'.format(how_module)] = tkinter.Label(window_47, text='FF')
    globals()['KS{}'.format(how_module)] = tkinter.Label(window_47, text='FF')
    globals()['P_in{}'.format(how_module)] = tkinter.Label(window_47, text='O_o')
    globals()['P_out{}'.format(how_module)] = tkinter.Label(window_47, text='FF')
    globals()['P_mirrow{}'.format(how_module)] = tkinter.Label(window_47, text='FF')
    globals()['code_fi{}'.format(how_module)] = tkinter.Label(window_47, text='FF')
    globals()['code_fi_man{}'.format(how_module)] = tkinter.Label(window_47, text='FF')

    param_label.place(x=0, y=20)

    globals()['s_number{}'.format(how_module)].place(x=170, y=20)
    globals()['version_p{}'.format(how_module)].place(x=170, y=51)
    globals()['time_work{}'.format(how_module)].place(x=170, y=82)
    globals()['time_work_min{}'.format(how_module)].place(x=170, y=112)
    globals()['temperature{}'.format(how_module)].place(x=170, y=142)
    globals()['voltage{}'.format(how_module)].place(x=170, y=172)
    globals()['KS{}'.format(how_module)].place(x=170, y=202)
    globals()['P_in{}'.format(how_module)].place(x=170, y=232)
    globals()['P_out{}'.format(how_module)].place(x=170, y=262)
    globals()['P_mirrow{}'.format(how_module)].place(x=170, y=292)
    globals()['code_fi{}'.format(how_module)].place(x=170, y=322)
    globals()['code_fi_man{}'.format(how_module)].place(x=170, y=352)
    globals()['update47{}'.format(how_module)] = threading.Thread(target=update_window_47, args=str(how_module), daemon=True)
    globals()['update47{}'.format(how_module)].start()
    window_47.mainloop()


def window49(how_module):
    global P_mirrow_1
    window_49 = tkinter.Tk()
    window_49.title('Параметры {} модуля'.format(how_module+1))
    window_49.geometry('400x450')

    param_label = tkinter.Label(window_49, justify='right', text='Серийный номер:\n\n'
                                                                 'Версия прошивки:\n\n'
                                                                 'Время работы, ч:\n\n'
                                                                 'Время работы, мин:\n\n'
                                                                 'Температура, ºC:\n\n'
                                                                 'Напряжение питания, В:\n\n\n'
                                                                 'Входная мощность, у.е.:\n\n'
                                                                 'Выходная мощность, у.е.:\n\n'
                                                                 'Отражённая мощность, у.е.:\n\n\n'
                                                                 'Текущий код фазы:\n\n'
                                                                 'Заводской код фазы:\n\n'
                                                                 'Текущий код атт.:\n\n'
                                                                 'Заводской код атт.:')
    channels_label_1 = tkinter.Label(window_49, text='Канал 1  |  Канал 2')
    KS_label = tkinter.Label(window_49, text='Контрольное слово')
    channels_label_2 = tkinter.Label(window_49, text='Канал 1:\n\n'
                                                     'Канал 2:\n\n')

    globals()['s_number{}'.format(how_module)] = tkinter.Label(window_49, text='FF')
    globals()['version_p{}'.format(how_module)] = tkinter.Label(window_49, text='FF')
    globals()['time_work{}'.format(how_module)] = tkinter.Label(window_49, text='FF')
    globals()['temperature{}'.format(how_module)] = tkinter.Label(window_49, text='FF')
    globals()['time_work_min{}'.format(how_module)] = tkinter.Label(window_49, text='FF')
    globals()['voltage{}'.format(how_module)] = tkinter.Label(window_49, text='FF')
    globals()['KS_1{}'.format(how_module)] = tkinter.Label(window_49, text='FF')
    globals()['KS_2{}'.format(how_module)] = tkinter.Label(window_49, text='FF')
    globals()['P_in_1{}'.format(how_module)] = tkinter.Label(window_49, text='O_o')
    globals()['P_out_1{}'.format(how_module)] = tkinter.Label(window_49, text='FF')
    globals()['P_mirrow_1{}'.format(how_module)] = tkinter.Label(window_49, text='FF')
    globals()['P_in_2{}'.format(how_module)] = tkinter.Label(window_49, text='O_o')
    globals()['P_out_2{}'.format(how_module)] = tkinter.Label(window_49, text='FF')
    globals()['P_mirrow_2{}'.format(how_module)] = tkinter.Label(window_49, text='FF')
    globals()['code_fi_1{}'.format(how_module)] = tkinter.Label(window_49, text='FF')
    globals()['code_fi_man_1{}'.format(how_module)] = tkinter.Label(window_49, text='FF')
    globals()['code_fi_2{}'.format(how_module)] = tkinter.Label(window_49, text='FF')
    globals()['code_fi_man_2{}'.format(how_module)] = tkinter.Label(window_49, text='FF')
    globals()['code_att_1{}'.format(how_module)] = tkinter.Label(window_49, text='FF')
    globals()['code_att_man_1{}'.format(how_module)] = tkinter.Label(window_49, text='FF')
    globals()['code_att_2{}'.format(how_module)] = tkinter.Label(window_49, text='FF')
    globals()['code_att_man_2{}'.format(how_module)] = tkinter.Label(window_49, text='FF')

    param_label.place(x=0, y=20)
    channels_label_1.place(x=200, y=192)
    channels_label_2.place(x=240, y=50)

    globals()['s_number{}'.format(how_module)].place(x=170, y=20)
    globals()['version_p{}'.format(how_module)].place(x=170, y=51)
    globals()['time_work{}'.format(how_module)].place(x=170, y=82)
    globals()['time_work_min{}'.format(how_module)].place(x=170, y=112)
    globals()['temperature{}'.format(how_module)].place(x=170, y=142)
    globals()['voltage{}'.format(how_module)].place(x=170, y=172)
    KS_label.place(x=250, y=20)
    globals()['KS_1{}'.format(how_module)].place(x=300, y=50)
    globals()['KS_2{}'.format(how_module)].place(x=300, y=80)
    globals()['P_in_1{}'.format(how_module)].place(x=200, y=217)
    globals()['P_out_1{}'.format(how_module)].place(x=200, y=247)
    globals()['P_mirrow_1{}'.format(how_module)].place(x=200, y=277)
    globals()['P_in_2{}'.format(how_module)].place(x=260, y=217)
    globals()['P_out_2{}'.format(how_module)].place(x=260, y=247)
    globals()['P_mirrow_2{}'.format(how_module)].place(x=260, y=277)
    globals()['code_fi_1{}'.format(how_module)].place(x=200, y=321)
    globals()['code_fi_man_1{}'.format(how_module)].place(x=200, y=351)
    globals()['code_fi_2{}'.format(how_module)].place(x=260, y=321)
    globals()['code_fi_man_2{}'.format(how_module)].place(x=260, y=351)
    globals()['code_att_1{}'.format(how_module)].place(x=200, y=381)
    globals()['code_att_man_1{}'.format(how_module)].place(x=200, y=411)
    globals()['code_att_2{}'.format(how_module)].place(x=260, y=381)
    globals()['code_att_man_2{}'.format(how_module)].place(x=260, y=411)
    globals()['update49{}'.format(how_module)] = threading.Thread(target=update_window_49, args=str(how_module), daemon=True)
    globals()['update49{}'.format(how_module)].start()
    window_49.mainloop()


def window51(how_module):
    global P_mirrow_2
    window_51 = tkinter.Tk()
    window_51.title('Параметры {} модуля'.format(how_module+1))
    window_51.geometry('430x470')
    param_label = tkinter.Label(window_51, justify='right', text='Серийный номер:\n\n'
                                                                 'Версия прошивки:\n\n'
                                                                 'Время работы, ч:\n\n'
                                                                 'Время работы, мин:\n\n'
                                                                 'Температура, ºC:\n\n'
                                                                 'Напряжение питания, В:\n\n\n\n'
                                                                 'Входная мощность, у.е.:\n\n'
                                                                 'Выходная мощность, у.е.:\n\n'
                                                                 'Отражённая мощность, у.е.:\n\n\n'
                                                                 'Текущий код фазы:\n\n'
                                                                 'Заводской код фазы:\n\n\n'
                                                                 'Текущий код атт:\n\n'
                                                                 'Заводской код атт:\n\n')
    channels_label_1 = tkinter.Label(window_51, text='Канал 1  |  Канал 2  |  Канал 3  |  Канал 4')
    KS_label = tkinter.Label(window_51, text='Контрольное слово')
    channels_label_2 = tkinter.Label(window_51, text='Канал 1:\n\n'
                                                     'Канал 2:\n\n'
                                                     'Канал 3:\n\n'
                                                     'Канал 4:')

    globals()['s_number{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['version_p{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['time_work{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['temperature{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['time_work_min{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['voltage{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['KS_1{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['KS_2{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['KS_3{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['KS_4{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['P_in_1{}'.format(how_module)] = tkinter.Label(window_51, text='O_o')
    globals()['P_out_1{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['P_mirrow_1{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['P_in_2{}'.format(how_module)] = tkinter.Label(window_51, text='O_o')
    globals()['P_out_2{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['P_mirrow_2{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['P_in_3{}'.format(how_module)] = tkinter.Label(window_51, text='O_o')
    globals()['P_out_3{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['P_mirrow_3{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['P_in_4{}'.format(how_module)] = tkinter.Label(window_51, text='O_o')
    globals()['P_out_4{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['P_mirrow_4{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_fi_1{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_fi_man_1{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_fi_2{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_fi_man_2{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_fi_3{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_fi_man_3{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_fi_41{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_fi_man_4{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_att_1{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_att_man_1{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_att_2{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_att_man_2{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_att_3{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_att_man_3{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_att_4{}'.format(how_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_att_man_4{}'.format(how_module)] = tkinter.Label(window_51, text='FF')

    param_label.place(x=0, y=20)
    channels_label_1.place(x=190, y=207)
    channels_label_2.place(x=240, y=50)

    globals()['s_number{}'.format(how_module)].place(x=170, y=20)
    globals()['version_p{}'.format(how_module)].place(x=170, y=51)
    globals()['time_work{}'.format(how_module)].place(x=170, y=82)
    globals()['time_work_min{}'.format(how_module)].place(x=170, y=112)
    globals()['temperature{}'.format(how_module)].place(x=170, y=142)
    globals()['voltage{}'.format(how_module)].place(x=170, y=172)
    KS_label.place(x=250, y=20)
    globals()['KS_1{}'.format(how_module)].place(x=300, y=50)
    globals()['KS_2{}'.format(how_module)].place(x=300, y=80)
    globals()['KS_3{}'.format(how_module)].place(x=300, y=110)
    globals()['KS_4{}'.format(how_module)].place(x=300, y=140)
    globals()['P_in_1{}'.format(how_module)].place(x=200, y=232)
    globals()['P_out_1{}'.format(how_module)].place(x=200, y=262)
    globals()['P_mirrow_1{}'.format(how_module)].place(x=200, y=292)
    globals()['P_in_2{}'.format(how_module)].place(x=260, y=232)
    globals()['P_out_2{}'.format(how_module)].place(x=260, y=262)
    globals()['P_mirrow_2{}'.format(how_module)].place(x=260, y=292)
    globals()['P_in_3{}'.format(how_module)].place(x=320, y=232)
    globals()['P_out_3{}'.format(how_module)].place(x=320, y=262)
    globals()['P_mirrow_3{}'.format(how_module)].place(x=320, y=292)
    globals()['P_in_4{}'.format(how_module)].place(x=375, y=232)
    globals()['P_out_4{}'.format(how_module)].place(x=375, y=262)
    globals()['P_mirrow_4{}'.format(how_module)].place(x=375, y=292)
    globals()['code_fi_1{}'.format(how_module)].place(x=200, y=337)
    globals()['code_fi_man_1{}'.format(how_module)].place(x=200, y=367)
    globals()['code_fi_2{}'.format(how_module)].place(x=260, y=337)
    globals()['code_fi_man_2{}'.format(how_module)].place(x=260, y=367)
    globals()['code_fi_3{}'.format(how_module)].place(x=320, y=337)
    globals()['code_fi_man_3{}'.format(how_module)].place(x=320, y=367)
    globals()['code_fi_41{}'.format(how_module)].place(x=375, y=337)
    globals()['code_fi_man_4{}'.format(how_module)].place(x=375, y=367)
    globals()['code_att_1{}'.format(how_module)].place(x=200, y=412)
    globals()['code_att_man_1{}'.format(how_module)].place(x=200, y=442)
    globals()['code_att_2{}'.format(how_module)].place(x=260, y=412)
    globals()['code_att_man_2{}'.format(how_module)].place(x=260, y=442)
    globals()['code_att_3{}'.format(how_module)].place(x=320, y=412)
    globals()['code_att_man_3{}'.format(how_module)].place(x=320, y=442)
    globals()['code_att_4{}'.format(how_module)].place(x=375, y=412)
    globals()['code_att_man_4{}'.format(how_module)].place(x=375, y=442)
    globals()['update51{}'.format(how_module)] = threading.Thread(target=update_window_51, args=(str(how_module)),
                                                                  daemon=True)
    globals()['update51{}'.format(how_module)].start()
    window_51.mainloop()


def update_window_47(how_module):
    while True:
        if len(opros.answers[int(how_module)]) > 10:
            globals()['s_number{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][26:32], 16)
            globals()['version_p{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][38:40], 16)
            globals()['time_work{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][32:36], 16)
            globals()['temperature{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][14:16], 16)
            globals()['time_work_min{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][36:38], 16)
            globals()['voltage{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][16:18], 16)
            globals()['KS{}'.format(how_module)]['text'] = bin(int(opros.answers[int(how_module)][18:20], 16))[1:] \
                                                           + '    '\
                                                           + bin(int(opros.answers[int(how_module)][20:22], 16))[1:]
            globals()['P_in{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][8:10], 16)
            globals()['P_out{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][10:12], 16)
            globals()['P_mirrow{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][12:14], 16)
            globals()['code_fi{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][22:24], 16)
            globals()['code_fi_man{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][24:26], 16)
        else:
            globals()['s_number{}'.format(how_module)]['text'] = '(¬_¬) не отвечает'
            globals()['s_number{}'.format(how_module)]['fg'] = 'red'
            globals()['version_p{}'.format(how_module)]['text'] = 'O0oₒ(¯º ¯)у~~'
            globals()['time_work{}'.format(how_module)]['text'] = '(ϭ_ϭ)'
        time.sleep(0.1)


def update_window_49(how_module):
    while True:
        if len(opros.answers[int(how_module)]) > 10:
            globals()['s_number{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][48:54], 16)
            globals()['version_p{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][60:62], 16)
            globals()['time_work{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][54:58], 16)
            globals()['temperature{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][14:16], 16)
            globals()['time_work_min{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][58:60], 16)
            globals()['voltage{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][16:18], 16)
            globals()['KS_1{}'.format(how_module)]['text'] = bin(int(opros.answers[int(how_module)][18:20], 16))[1:] \
                                                           + '    '\
                                                           + bin(int(opros.answers[int(how_module)][20:22], 16))[1:]
            globals()['KS_2{}'.format(how_module)]['text'] = bin(int(opros.answers[int(how_module)][36:38], 16))[1:] \
                                                           + '    '\
                                                           + bin(int(opros.answers[int(how_module)][38:40], 16))[1:]
            globals()['P_in_1{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][8:10], 16)
            globals()['P_out_1{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][10:12], 16)
            globals()['P_mirrow_1{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][12:14], 16)
            globals()['P_in_2{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][30:32], 16)
            globals()['P_out_2{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][32:34], 16)
            globals()['P_mirrow_2{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][34:36], 16)
            globals()['code_fi_1{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][22:24], 16)
            globals()['code_fi_man_1{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][24:26], 16)
            globals()['code_fi_2{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][40:42], 16)
            globals()['code_fi_man_2{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][42:44], 16)
            globals()['code_att_1{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][26:28], 16)
            globals()['code_att_man_1{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][28:30], 16)
            globals()['code_att_2{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][44:46], 16)
            globals()['code_att_man_2{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][46:48], 16)
        else:
            globals()['temperature{}'.format(how_module)]['text'] = '(ノ º□º)ノ ⌒ ┴----┴'
            globals()['version_p{}'.format(how_module)]['text'] = '¯\(°_0)/¯'
            globals()['time_work{}'.format(how_module)]['text'] = 'обмена нет'
            globals()['time_work{}'.format(how_module)]['fg'] = 'red'
        time.sleep(0.1)


def update_window_51(how_module):
    while True:
        if len(opros.answers[int(how_module)]) > 10:
            globals()['s_number{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][14:22], 16)
            globals()['version_p{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][28:30], 16)
            globals()['time_work{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][22:26], 16)
            globals()['temperature{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][10:12], 16)
            globals()['time_work_min{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][26:28], 16)
            globals()['voltage{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][12:14], 16)
            globals()['KS_1{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][36:40], 16)
            globals()['KS_2{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][54:58], 16)
            globals()['KS_3{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][72:76], 16)
            globals()['KS_4{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][90:94], 16)
            globals()['P_in_1{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][30:32], 16)
            globals()['P_out_1{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][32:34], 16)
            globals()['P_mirrow_1{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][34:36], 16)
            globals()['P_in_2{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][48:50], 16)
            globals()['P_out_2{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][50:52], 16)
            globals()['P_mirrow_2{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][52:54], 16)
            globals()['P_in_3{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][66:68], 16)
            globals()['P_out_3{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][68:70], 16)
            globals()['P_mirrow_3{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][70:72], 16)
            globals()['P_in_4{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][84:86], 16)
            globals()['P_out_4{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][86:88], 16)
            globals()['P_mirrow_4{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][88:90], 16)
            globals()['code_fi_1{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][40:42], 16)
            globals()['code_fi_man_1{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][42:44], 16)
            globals()['code_fi_2{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][58:60], 16)
            globals()['code_fi_man_2{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][60:62], 16)
            globals()['code_fi_3{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][76:78], 16)
            globals()['code_fi_man_3{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][78:80], 16)
            globals()['code_fi_41{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][94:96], 16)
            globals()['code_fi_man_4{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][96:98], 16)
            globals()['code_att_1{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][44:46], 16)
            globals()['code_att_man_1{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][46:48], 16)
            globals()['code_att_2{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][62:64], 16)
            globals()['code_att_man_2{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][64:66], 16)
            globals()['code_att_3{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][80:82], 16)
            globals()['code_att_man_3{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][82:84], 16)
            globals()['code_att_4{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][98:100], 16)
            globals()['code_att_man_4{}'.format(how_module)]['text'] = int(opros.answers[int(how_module)][100:102], 16)
        else:
            globals()['KS_1{}'.format(how_module)]['text'] = '(ノ º□º)ノ ⌒ ┴----┴'
            globals()['KS_2{}'.format(how_module)]['text'] = '¯\(°_0)/¯'
            globals()['KS_3{}'.format(how_module)]['text'] = 'обмена нет'
            globals()['KS_3{}'.format(how_module)]['fg'] = 'red'
        time.sleep(0.1)


if __name__ == '__main__':
    pass
