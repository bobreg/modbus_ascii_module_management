import tkinter
import threading
import opros
import time


def full_information_of_module(type_window, what_module):
    if type_window == '47':
        window47(what_module)
    if type_window == '49':
        window49(what_module)
    if type_window == '51':
        window51(what_module)


def create_string_KSs(KS):
    ksb = list(bin(int(KS, 16))[2:])
    ksb = ['0' for i in range(8 - len(ksb))] + ksb
    return ksb


def window47(what_module):
    global P_mirrow
    window_47 = tkinter.Tk()
    window_47.title('Параметры {} модуля'.format(what_module+1))
    window_47.geometry('430x430')

    param_label = tkinter.Label(window_47, justify='right', text='Серийный номер:\n\n'
                                                                 'Версия прошивки:\n\n'
                                                                 'Время работы, ч:\n\n'
                                                                 'Время работы, мин:\n\n'
                                                                 'Температура, ºC:\n\n'
                                                                 'Напряжение питания, В:\n\n'
                                                                 'Входная мощность, у.е.:\n\n'
                                                                 'Выходная мощность, у.е.:\n\n'
                                                                 'Отражённая мощность, у.е.:\n\n'
                                                                 'Текущий код фазы:\n\n'
                                                                 'Заводской код фазы:\n\n'
                                                                 'Контрольное слово:')
    state_label1 = tkinter.Label(window_47, justify='center', text='Состояние модуля\nпо контрольному слову', font='Verdana 8 bold')
    state_label2 = tkinter.Label(window_47, justify='right', text='Сеть ВКЛ\n\n'
                                                                 'ИП ВКЛ\n\n'
                                                                 'СВЧ тракт открыт\n\n'
                                                                 'Рвх меньше нормы\n\n'
                                                                 'Рвх больше нормы\n\n'
                                                                 'Рвых меньше нормы\n\n'
                                                                 'Ротр больше нормы\n\n'
                                                                 'Перегрев\n\n'
                                                                 'Перегрузка по T/Q\n\n'
                                                                 'Нет имп.упр\n\n'
                                                                 'Авария пит.\n\n'
                                                                 'Неиспр. датчик tºC')
    ksb1 = tkinter.Label(window_47, text='Первый байт')
    ksb2 = tkinter.Label(window_47, text='Второй байт:')
    granica = tkinter.Canvas(window_47, width=3, height=400, bg='black')
    for i in range(12):
        globals()['state{}{}'.format(i, what_module)]= tkinter.Canvas(window_47, width=20, height=20, bg='blue')

    globals()['s_number{}'.format(what_module)] = tkinter.Label(window_47, text='FF')
    globals()['version_p{}'.format(what_module)] = tkinter.Label(window_47, text='FF')
    globals()['time_work{}'.format(what_module)] = tkinter.Label(window_47, text='FF')
    globals()['temperature{}'.format(what_module)] = tkinter.Label(window_47, text='FF')
    globals()['time_work_min{}'.format(what_module)] = tkinter.Label(window_47, text='FF')
    globals()['voltage{}'.format(what_module)] = tkinter.Label(window_47, text='FF')
    globals()['KS1b1{}'.format(what_module)] = tkinter.Label(window_47, text='FF')
    globals()['KS1b2{}'.format(what_module)] = tkinter.Label(window_47, text='FF')
    globals()['P_in{}'.format(what_module)] = tkinter.Label(window_47, text='O_o')
    globals()['P_out{}'.format(what_module)] = tkinter.Label(window_47, text='FF')
    globals()['P_mirrow{}'.format(what_module)] = tkinter.Label(window_47, text='FF')
    globals()['code_fi{}'.format(what_module)] = tkinter.Label(window_47, text='FF')
    globals()['code_fi_man{}'.format(what_module)] = tkinter.Label(window_47, text='FF')

    param_label.place(x=0, y=20)
    state_label1.place(x=250, y=5)
    state_label2.place(x=230, y=40)
    ksb1.place(x=53, y=372)
    ksb2.place(x=53, y=392)
    granica.place(x=220, y=0)
    for i in range(12):
        globals()['state{}{}'.format(i, what_module)].place(x=360, y=40 + i * 30)

    globals()['s_number{}'.format(what_module)].place(x=170, y=20)
    globals()['version_p{}'.format(what_module)].place(x=170, y=51)
    globals()['time_work{}'.format(what_module)].place(x=170, y=82)
    globals()['time_work_min{}'.format(what_module)].place(x=170, y=112)
    globals()['temperature{}'.format(what_module)].place(x=170, y=142)
    globals()['voltage{}'.format(what_module)].place(x=170, y=172)
    globals()['KS1b1{}'.format(what_module)].place(x=140, y=372)
    globals()['KS1b2{}'.format(what_module)].place(x=140, y=392)
    globals()['P_in{}'.format(what_module)].place(x=170, y=202)
    globals()['P_out{}'.format(what_module)].place(x=170, y=232)
    globals()['P_mirrow{}'.format(what_module)].place(x=170, y=262)
    globals()['code_fi{}'.format(what_module)].place(x=170, y=292)
    globals()['code_fi_man{}'.format(what_module)].place(x=170, y=322)
    globals()['update47{}'.format(what_module)] = threading.Thread(target=update_window_47, args=str(what_module), daemon=True)
    globals()['update47{}'.format(what_module)].start()
    window_47.mainloop()


def window49(what_module):
    global P_mirrow_1
    window_49 = tkinter.Tk()
    window_49.title('Параметры {} модуля'.format(what_module+1))
    window_49.geometry('520x600')

    param_label1 = tkinter.Label(window_49, justify='right', text='Серийный номер:\n\n'
                                                                 'Версия прошивки:\n\n'
                                                                 'Время работы, ч:\n\n'
                                                                 'Время работы, мин:\n\n'
                                                                 'Температура, ºC:\n\n'
                                                                 'Напряжение питания, В:')

    param_label2 = tkinter.Label(window_49, justify='right', text='Входная мощность, у.е.:\n\n'
                                                                 'Выходная мощность, у.е.:\n\n'
                                                                 'Отражённая мощность, у.е.:\n\n\n'
                                                                 'Текущий код фазы:\n\n'
                                                                 'Заводской код фазы:\n\n'
                                                                 'Текущий код атт.:\n\n'
                                                                 'Заводской код атт.:')
    channels_label_1 = tkinter.Label(window_49, text='Канал 1  |  Канал 2', font='arial 8 bold')
    channels_label_2 = tkinter.Label(window_49, text='Канал 1  |  Канал 2', font='arial 8 bold')
    channels_label_3 = tkinter.Label(window_49, text='Канал 1\n'
                                                     'Байт 1:\n'
                                                     'Байт 2:\n\n'
                                                     'Канал 2\n'
                                                     'Байт 1:\n'
                                                     'Байт 2:\n')
    state_label1 = tkinter.Label(window_49, justify='center', text='Состояние модуля\nпо контрольному слову',
                                 font='Verdana 8 bold')
    state_label2 = tkinter.Label(window_49, justify='right', text='Сеть ВКЛ\n\n'
                                                                  'ИП ВКЛ\n\n'
                                                                  'СВЧ тракт открыт\n\n'
                                                                  'Рвх меньше нормы\n\n'
                                                                  'Рвх больше нормы\n\n'
                                                                  'Рвых меньше нормы\n\n'
                                                                  'Ротр больше нормы\n\n'
                                                                  'Перегрев\n\n'
                                                                  'Перегрузка по T/Q\n\n'
                                                                  'Нет имп.упр\n\n'
                                                                  'Авария пит.\n\n'
                                                                  'Неиспр. датчик tºC')

    granica = tkinter.Canvas(window_49, width=3, height=470, bg='black')
    for i in range(12):
        globals()['state_ks1_49{}{}'.format(i, what_module)]= tkinter.Canvas(window_49, width=20, height=20, bg='blue')
    for i in range(12):
        globals()['state_ks2_49{}{}'.format(i, what_module)]= tkinter.Canvas(window_49, width=20, height=20, bg='blue')
    KS_label = tkinter.Label(window_49, text='Контрольное слово', font='arial 8 bold')

    globals()['s_number{}'.format(what_module)] = tkinter.Label(window_49, text='FF')
    globals()['version_p{}'.format(what_module)] = tkinter.Label(window_49, text='FF')
    globals()['time_work{}'.format(what_module)] = tkinter.Label(window_49, text='FF')
    globals()['temperature{}'.format(what_module)] = tkinter.Label(window_49, text='FF')
    globals()['time_work_min{}'.format(what_module)] = tkinter.Label(window_49, text='FF')
    globals()['voltage{}'.format(what_module)] = tkinter.Label(window_49, text='FF')
    globals()['KS_1b1{}'.format(what_module)] = tkinter.Label(window_49, text='FF')
    globals()['KS_1b2{}'.format(what_module)] = tkinter.Label(window_49, text='FF')
    globals()['KS_2b1{}'.format(what_module)] = tkinter.Label(window_49, text='FF')
    globals()['KS_2b2{}'.format(what_module)] = tkinter.Label(window_49, text='FF')
    globals()['P_in_1{}'.format(what_module)] = tkinter.Label(window_49, text='O_o')
    globals()['P_out_1{}'.format(what_module)] = tkinter.Label(window_49, text='FF')
    globals()['P_mirrow_1{}'.format(what_module)] = tkinter.Label(window_49, text='FF')
    globals()['P_in_2{}'.format(what_module)] = tkinter.Label(window_49, text='O_o')
    globals()['P_out_2{}'.format(what_module)] = tkinter.Label(window_49, text='FF')
    globals()['P_mirrow_2{}'.format(what_module)] = tkinter.Label(window_49, text='FF')
    globals()['code_fi_1{}'.format(what_module)] = tkinter.Label(window_49, text='FF')
    globals()['code_fi_man_1{}'.format(what_module)] = tkinter.Label(window_49, text='FF')
    globals()['code_fi_2{}'.format(what_module)] = tkinter.Label(window_49, text='FF')
    globals()['code_fi_man_2{}'.format(what_module)] = tkinter.Label(window_49, text='FF')
    globals()['code_att_1{}'.format(what_module)] = tkinter.Label(window_49, text='FF')
    globals()['code_att_man_1{}'.format(what_module)] = tkinter.Label(window_49, text='FF')
    globals()['code_att_2{}'.format(what_module)] = tkinter.Label(window_49, text='FF')
    globals()['code_att_man_2{}'.format(what_module)] = tkinter.Label(window_49, text='FF')

    param_label1.place(x=70, y=20)
    param_label2.place(x=0, y=237)
    channels_label_1.place(x=150, y=212)
    channels_label_2.place(x=400, y=40)
    channels_label_3.place(x=70, y=481)
    state_label1.place(x=300, y=5)
    state_label2.place(x=270, y=80)
    granica.place(x=260, y=0)
    for i in range(12):
        globals()['state_ks1_49{}{}'.format(i, what_module)].place(x=420, y=80 + i * 30)
    for i in range(12):
        globals()['state_ks2_49{}{}'.format(i, what_module)].place(x=470, y=80 + i * 30)

    globals()['s_number{}'.format(what_module)].place(x=220, y=20)
    globals()['version_p{}'.format(what_module)].place(x=220, y=51)
    globals()['time_work{}'.format(what_module)].place(x=220, y=82)
    globals()['time_work_min{}'.format(what_module)].place(x=220, y=112)
    globals()['temperature{}'.format(what_module)].place(x=220, y=142)
    globals()['voltage{}'.format(what_module)].place(x=220, y=172)
    KS_label.place(x=70, y=461)
    globals()['KS_1b1{}'.format(what_module)].place(x=120, y=496)
    globals()['KS_1b2{}'.format(what_module)].place(x=120, y=511)
    globals()['KS_2b1{}'.format(what_module)].place(x=120, y=556)
    globals()['KS_2b2{}'.format(what_module)].place(x=120, y=571)
    globals()['P_in_1{}'.format(what_module)].place(x=170, y=237)
    globals()['P_out_1{}'.format(what_module)].place(x=170, y=267)
    globals()['P_mirrow_1{}'.format(what_module)].place(x=170, y=297)
    globals()['P_in_2{}'.format(what_module)].place(x=230, y=237)
    globals()['P_out_2{}'.format(what_module)].place(x=230, y=267)
    globals()['P_mirrow_2{}'.format(what_module)].place(x=230, y=297)
    globals()['code_fi_1{}'.format(what_module)].place(x=170, y=341)
    globals()['code_fi_man_1{}'.format(what_module)].place(x=170, y=371)
    globals()['code_fi_2{}'.format(what_module)].place(x=230, y=341)
    globals()['code_fi_man_2{}'.format(what_module)].place(x=230, y=371)
    globals()['code_att_1{}'.format(what_module)].place(x=170, y=401)
    globals()['code_att_man_1{}'.format(what_module)].place(x=170, y=431)
    globals()['code_att_2{}'.format(what_module)].place(x=230, y=401)
    globals()['code_att_man_2{}'.format(what_module)].place(x=230, y=431)
    globals()['update49{}'.format(what_module)] = threading.Thread(target=update_window_49, args=str(what_module),
                                                                   daemon=True)
    globals()['update49{}'.format(what_module)].start()
    window_49.mainloop()


def window51(what_module):
    global P_mirrow_2
    window_51 = tkinter.Tk()
    window_51.title('Параметры {} модуля'.format(what_module+1))
    window_51.geometry('800x480')
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
    channels_label_1 = tkinter.Label(window_51, text='Канал 1  |  Канал 2  |  Канал 3  |  Канал 4', font='arial 8 bold')
    channels_label_2 = tkinter.Label(window_51, text='Канал 1:\n\n'
                                                     'Канал 2:\n\n'
                                                     'Канал 3:\n\n'
                                                     'Канал 4:', font='arial 8 bold')
    channels_label_3 = tkinter.Label(window_51, text='Канал 1  |  Канал 2  |  Канал 3  |  Канал 4', font='arial 8 bold')
    KS_label = tkinter.Label(window_51, text='Контрольное слово')
    state_label1 = tkinter.Label(window_51, justify='center', text='Состояние модуля\nпо контрольному слову',
                                 font='italicc 10 bold')
    state_label2 = tkinter.Label(window_51, justify='right', text='Сеть ВКЛ\n\n'
                                                                  'ИП ВКЛ\n\n'
                                                                  'СВЧ тракт открыт\n\n'
                                                                  'Рвх меньше нормы\n\n'
                                                                  'Рвх больше нормы\n\n'
                                                                  'Рвых меньше нормы\n\n'
                                                                  'Ротр больше нормы\n\n'
                                                                  'Перегрев\n\n'
                                                                  'Перегрузка по T/Q\n\n'
                                                                  'Нет имп.упр\n\n'
                                                                  'Авария пит.\n\n'
                                                                  'Неиспр. датчик tºC')
    granica = tkinter.Canvas(window_51, width=3, height=470, bg='black')
    for i in range(12):
        globals()['state_ks1_51{}{}'.format(i, what_module)]= tkinter.Canvas(window_51, width=20, height=20, bg='blue')
    for i in range(12):
        globals()['state_ks2_51{}{}'.format(i, what_module)]= tkinter.Canvas(window_51, width=20, height=20, bg='blue')
    for i in range(12):
        globals()['state_ks3_51{}{}'.format(i, what_module)]= tkinter.Canvas(window_51, width=20, height=20, bg='blue')
    for i in range(12):
        globals()['state_ks4_51{}{}'.format(i, what_module)]= tkinter.Canvas(window_51, width=20, height=20, bg='blue')

    globals()['s_number{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['version_p{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['time_work{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['temperature{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['time_work_min{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['voltage{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['KS_1{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['KS_2{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['KS_3{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['KS_4{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['P_in_1{}'.format(what_module)] = tkinter.Label(window_51, text='O_o')
    globals()['P_out_1{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['P_mirrow_1{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['P_in_2{}'.format(what_module)] = tkinter.Label(window_51, text='O_o')
    globals()['P_out_2{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['P_mirrow_2{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['P_in_3{}'.format(what_module)] = tkinter.Label(window_51, text='O_o')
    globals()['P_out_3{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['P_mirrow_3{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['P_in_4{}'.format(what_module)] = tkinter.Label(window_51, text='O_o')
    globals()['P_out_4{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['P_mirrow_4{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_fi_1{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_fi_man_1{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_fi_2{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_fi_man_2{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_fi_3{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_fi_man_3{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_fi_41{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_fi_man_4{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_att_1{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_att_man_1{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_att_2{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_att_man_2{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_att_3{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_att_man_3{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_att_4{}'.format(what_module)] = tkinter.Label(window_51, text='FF')
    globals()['code_att_man_4{}'.format(what_module)] = tkinter.Label(window_51, text='FF')

    param_label.place(x=0, y=20)
    channels_label_1.place(x=190, y=207)
    channels_label_2.place(x=240, y=50)
    channels_label_3.place(x=560, y=50)
    state_label1.place(x=560, y=5)
    state_label2.place(x=430, y=80)
    granica.place(x=420, y=0)
    for i in range(12):
        globals()['state_ks1_51{}{}'.format(i, what_module)].place(x=570, y=80 + i * 30)
    for i in range(12):
        globals()['state_ks2_51{}{}'.format(i, what_module)].place(x=630, y=80 + i * 30)
    for i in range(12):
        globals()['state_ks3_51{}{}'.format(i, what_module)].place(x=690, y=80 + i * 30)
    for i in range(12):
        globals()['state_ks4_51{}{}'.format(i, what_module)].place(x=750, y=80 + i * 30)

    globals()['s_number{}'.format(what_module)].place(x=170, y=20)
    globals()['version_p{}'.format(what_module)].place(x=170, y=51)
    globals()['time_work{}'.format(what_module)].place(x=170, y=82)
    globals()['time_work_min{}'.format(what_module)].place(x=170, y=112)
    globals()['temperature{}'.format(what_module)].place(x=170, y=142)
    globals()['voltage{}'.format(what_module)].place(x=170, y=172)
    KS_label.place(x=250, y=20)
    globals()['KS_1{}'.format(what_module)].place(x=300, y=50)
    globals()['KS_2{}'.format(what_module)].place(x=300, y=80)
    globals()['KS_3{}'.format(what_module)].place(x=300, y=110)
    globals()['KS_4{}'.format(what_module)].place(x=300, y=140)
    globals()['P_in_1{}'.format(what_module)].place(x=200, y=232)
    globals()['P_out_1{}'.format(what_module)].place(x=200, y=262)
    globals()['P_mirrow_1{}'.format(what_module)].place(x=200, y=292)
    globals()['P_in_2{}'.format(what_module)].place(x=260, y=232)
    globals()['P_out_2{}'.format(what_module)].place(x=260, y=262)
    globals()['P_mirrow_2{}'.format(what_module)].place(x=260, y=292)
    globals()['P_in_3{}'.format(what_module)].place(x=320, y=232)
    globals()['P_out_3{}'.format(what_module)].place(x=320, y=262)
    globals()['P_mirrow_3{}'.format(what_module)].place(x=320, y=292)
    globals()['P_in_4{}'.format(what_module)].place(x=375, y=232)
    globals()['P_out_4{}'.format(what_module)].place(x=375, y=262)
    globals()['P_mirrow_4{}'.format(what_module)].place(x=375, y=292)
    globals()['code_fi_1{}'.format(what_module)].place(x=200, y=337)
    globals()['code_fi_man_1{}'.format(what_module)].place(x=200, y=367)
    globals()['code_fi_2{}'.format(what_module)].place(x=260, y=337)
    globals()['code_fi_man_2{}'.format(what_module)].place(x=260, y=367)
    globals()['code_fi_3{}'.format(what_module)].place(x=320, y=337)
    globals()['code_fi_man_3{}'.format(what_module)].place(x=320, y=367)
    globals()['code_fi_41{}'.format(what_module)].place(x=375, y=337)
    globals()['code_fi_man_4{}'.format(what_module)].place(x=375, y=367)
    globals()['code_att_1{}'.format(what_module)].place(x=200, y=412)
    globals()['code_att_man_1{}'.format(what_module)].place(x=200, y=442)
    globals()['code_att_2{}'.format(what_module)].place(x=260, y=412)
    globals()['code_att_man_2{}'.format(what_module)].place(x=260, y=442)
    globals()['code_att_3{}'.format(what_module)].place(x=320, y=412)
    globals()['code_att_man_3{}'.format(what_module)].place(x=320, y=442)
    globals()['code_att_4{}'.format(what_module)].place(x=375, y=412)
    globals()['code_att_man_4{}'.format(what_module)].place(x=375, y=442)
    globals()['update51{}'.format(what_module)] = threading.Thread(target=update_window_51, args=(str(what_module)),
                                                                   daemon=True)
    globals()['update51{}'.format(what_module)].start()
    window_51.mainloop()


def update_window_47(what_module):
    while True:
        if len(opros.answers[int(what_module)]) > 10:
            globals()['s_number{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][26:32], 16)
            globals()['version_p{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][38:40], 16)
            globals()['time_work{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][32:36], 16)
            globals()['temperature{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][14:16], 16)
            globals()['time_work_min{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][36:38], 16)
            globals()['voltage{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][16:18], 16)
            globals()['P_in{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][8:10], 16)
            globals()['P_out{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][10:12], 16)
            globals()['P_mirrow{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][12:14], 16)
            globals()['code_fi{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][22:24], 16)
            globals()['code_fi_man{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][24:26], 16)

            ksb1 = create_string_KSs(opros.answers[int(what_module)][18:20])  # обработка аварийных байтов
            ksb2 = create_string_KSs(opros.answers[int(what_module)][20:22])
            globals()['KS1b1{}'.format(what_module)]['text'] = ksb1
            globals()['KS1b2{}'.format(what_module)]['text'] = ksb2
            for i in range(-1, -4, -1):
                if ksb2[i] == '1':
                    globals()['state{}{}'.format(-i - 1, what_module)]['bg'] = 'green'
                else:
                    globals()['state{}{}'.format(-i - 1, what_module)]['bg'] = 'blue'
            for i in range(-4, -9, -1):
                if ksb2[i] == '0':
                    globals()['state{}{}'.format(-i - 1, what_module)]['bg'] = 'green'
                else:
                    globals()['state{}{}'.format(-i - 1, what_module)]['bg'] = 'Red'
            for i in range(-9, -13, -1):
                if ksb1[i+8] == '0':
                    globals()['state{}{}'.format(-i-1, what_module)]['bg'] = 'green'
                else:
                    globals()['state{}{}'.format(-i-1, what_module)]['bg'] = 'Red'
        else:
            globals()['s_number{}'.format(what_module)]['text'] = '(¬_¬) не отвечает'
            globals()['s_number{}'.format(what_module)]['fg'] = 'red'
            globals()['version_p{}'.format(what_module)]['text'] = 'O0oₒ(¯º ¯)у~~'
            globals()['time_work{}'.format(what_module)]['text'] = '(ϭ_ϭ)'
        time.sleep(0.1)


def update_window_49(what_module):
    while True:
        if len(opros.answers[int(what_module)]) > 10:
            globals()['s_number{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][48:54], 16)
            globals()['version_p{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][60:62], 16)
            globals()['time_work{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][54:58], 16)
            globals()['temperature{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][14:16], 16)
            globals()['time_work_min{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][58:60], 16)
            globals()['voltage{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][16:18], 16)

            ks1b1 = create_string_KSs(opros.answers[int(what_module)][18:20])  # обработка аварийных байтов
            ks1b2 = create_string_KSs(opros.answers[int(what_module)][20:22])
            ks2b1 = create_string_KSs(opros.answers[int(what_module)][36:38])
            ks2b2 = create_string_KSs(opros.answers[int(what_module)][38:40])
            globals()['KS_1b1{}'.format(what_module)]['text'] = ks1b1
            globals()['KS_1b2{}'.format(what_module)]['text'] = ks1b2
            globals()['KS_2b1{}'.format(what_module)]['text'] = ks2b1
            globals()['KS_2b2{}'.format(what_module)]['text'] = ks2b2
            '''Первый столбик'''
            for i in range(-1, -4, -1):
                if ks1b2[i] == '1':
                    globals()['state_ks1_49{}{}'.format(-i - 1, what_module)]['bg'] = 'green'
                else:
                    globals()['state_ks1_49{}{}'.format(-i - 1, what_module)]['bg'] = 'blue'
            for i in range(-4, -9, -1):
                if ks1b2[i] == '0':
                    globals()['state_ks1_49{}{}'.format(-i - 1, what_module)]['bg'] = 'green'
                else:
                    globals()['state_ks1_49{}{}'.format(-i - 1, what_module)]['bg'] = 'Red'
            for i in range(-9, -13, -1):
                if ks1b1[i+8] == '0':
                    globals()['state_ks1_49{}{}'.format(-i-1, what_module)]['bg'] = 'green'
                else:
                    globals()['state_ks1_49{}{}'.format(-i-1, what_module)]['bg'] = 'Red'
            '''Второй столбик'''
            for i in range(-1, -4, -1):
                if ks2b2[i] == '1':
                    globals()['state_ks2_49{}{}'.format(-i - 1, what_module)]['bg'] = 'green'
                else:
                    globals()['state_ks2_49{}{}'.format(-i - 1, what_module)]['bg'] = 'blue'
            for i in range(-4, -9, -1):
                if ks2b2[i] == '0':
                    globals()['state_ks2_49{}{}'.format(-i - 1, what_module)]['bg'] = 'green'
                else:
                    globals()['state_ks2_49{}{}'.format(-i - 1, what_module)]['bg'] = 'Red'
            for i in range(-9, -13, -1):
                if ks2b1[i+8] == '0':
                    globals()['state_ks2_49{}{}'.format(-i-1, what_module)]['bg'] = 'green'
                else:
                    globals()['state_ks2_49{}{}'.format(-i-1, what_module)]['bg'] = 'Red'

            globals()['P_in_1{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][8:10], 16)
            globals()['P_out_1{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][10:12], 16)
            globals()['P_mirrow_1{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][12:14], 16)
            globals()['P_in_2{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][30:32], 16)
            globals()['P_out_2{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][32:34], 16)
            globals()['P_mirrow_2{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][34:36], 16)
            globals()['code_fi_1{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][22:24], 16)
            globals()['code_fi_man_1{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][24:26], 16)
            globals()['code_fi_2{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][40:42], 16)
            globals()['code_fi_man_2{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][42:44], 16)
            globals()['code_att_1{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][26:28], 16)
            globals()['code_att_man_1{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][28:30], 16)
            globals()['code_att_2{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][44:46], 16)
            globals()['code_att_man_2{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][46:48], 16)
        else:
            globals()['temperature{}'.format(what_module)]['text'] = '(ノ º□º)ノ ⌒ ┴----┴'
            globals()['version_p{}'.format(what_module)]['text'] = '¯\(°_0)/¯'
            globals()['time_work{}'.format(what_module)]['text'] = 'обмена нет'
            globals()['time_work{}'.format(what_module)]['fg'] = 'red'
        time.sleep(0.1)


def update_window_51(what_module):
    while True:
        if len(opros.answers[int(what_module)]) > 10:
            globals()['s_number{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][14:22], 16)
            globals()['version_p{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][28:30], 16)
            globals()['time_work{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][22:26], 16)
            globals()['temperature{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][10:12], 16)
            globals()['time_work_min{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][26:28], 16)
            globals()['voltage{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][12:14], 16)

            ks1b1 = create_string_KSs(opros.answers[int(what_module)][36:38])  # обработка аварийных байтов
            ks1b2 = create_string_KSs(opros.answers[int(what_module)][38:40])
            ks2b1 = create_string_KSs(opros.answers[int(what_module)][54:56])
            ks2b2 = create_string_KSs(opros.answers[int(what_module)][56:58])
            ks3b1 = create_string_KSs(opros.answers[int(what_module)][72:74])
            ks3b2 = create_string_KSs(opros.answers[int(what_module)][74:76])
            ks4b1 = create_string_KSs(opros.answers[int(what_module)][90:92])
            ks4b2 = create_string_KSs(opros.answers[int(what_module)][92:94])
            globals()['KS_1{}'.format(what_module)]['text'] = bin(int(opros.answers[int(what_module)][36:40], 16))
            globals()['KS_2{}'.format(what_module)]['text'] = bin(int(opros.answers[int(what_module)][54:58], 16))
            globals()['KS_3{}'.format(what_module)]['text'] = bin(int(opros.answers[int(what_module)][72:76], 16))
            globals()['KS_4{}'.format(what_module)]['text'] = bin(int(opros.answers[int(what_module)][90:94], 16))
            '''Первый столбик'''
            for i in range(-1, -4, -1):
                if ks1b2[i] == '1':
                    globals()['state_ks1_51{}{}'.format(-i - 1, what_module)]['bg'] = 'green'
                else:
                    globals()['state_ks1_51{}{}'.format(-i - 1, what_module)]['bg'] = 'blue'
            for i in range(-4, -9, -1):
                if ks1b2[i] == '0':
                    globals()['state_ks1_51{}{}'.format(-i - 1, what_module)]['bg'] = 'green'
                else:
                    globals()['state_ks1_51{}{}'.format(-i - 1, what_module)]['bg'] = 'Red'
            for i in range(-9, -13, -1):
                if ks1b1[i + 8] == '0':
                    globals()['state_ks1_51{}{}'.format(-i - 1, what_module)]['bg'] = 'green'
                else:
                    globals()['state_ks1_51{}{}'.format(-i - 1, what_module)]['bg'] = 'Red'
            '''Второй столбик'''
            for i in range(-1, -4, -1):
                if ks2b2[i] == '1':
                    globals()['state_ks2_51{}{}'.format(-i - 1, what_module)]['bg'] = 'green'
                else:
                    globals()['state_ks2_51{}{}'.format(-i - 1, what_module)]['bg'] = 'blue'
            for i in range(-4, -9, -1):
                if ks2b2[i] == '0':
                    globals()['state_ks2_51{}{}'.format(-i - 1, what_module)]['bg'] = 'green'
                else:
                    globals()['state_ks2_51{}{}'.format(-i - 1, what_module)]['bg'] = 'Red'
            for i in range(-9, -13, -1):
                if ks2b1[i + 8] == '0':
                    globals()['state_ks2_51{}{}'.format(-i - 1, what_module)]['bg'] = 'green'
                else:
                    globals()['state_ks2_51{}{}'.format(-i - 1, what_module)]['bg'] = 'Red'
            '''третий столбик'''
            for i in range(-1, -4, -1):
                if ks3b2[i] == '1':
                    globals()['state_ks3_51{}{}'.format(-i - 1, what_module)]['bg'] = 'green'
                else:
                    globals()['state_ks3_51{}{}'.format(-i - 1, what_module)]['bg'] = 'blue'
            for i in range(-4, -9, -1):
                if ks3b2[i] == '0':
                    globals()['state_ks3_51{}{}'.format(-i - 1, what_module)]['bg'] = 'green'
                else:
                    globals()['state_ks3_51{}{}'.format(-i - 1, what_module)]['bg'] = 'Red'
            for i in range(-9, -13, -1):
                if ks3b1[i+8] == '0':
                    globals()['state_ks3_51{}{}'.format(-i-1, what_module)]['bg'] = 'green'
                else:
                    globals()['state_ks3_51{}{}'.format(-i-1, what_module)]['bg'] = 'Red'
            '''четвёртый столбик'''
            for i in range(-1, -4, -1):
                if ks4b2[i] == '1':
                    globals()['state_ks4_51{}{}'.format(-i - 1, what_module)]['bg'] = 'green'
                else:
                    globals()['state_ks4_51{}{}'.format(-i - 1, what_module)]['bg'] = 'blue'
            for i in range(-4, -9, -1):
                if ks4b2[i] == '0':
                    globals()['state_ks4_51{}{}'.format(-i - 1, what_module)]['bg'] = 'green'
                else:
                    globals()['state_ks4_51{}{}'.format(-i - 1, what_module)]['bg'] = 'Red'
            for i in range(-9, -13, -1):
                if ks4b1[i+8] == '0':
                    globals()['state_ks4_51{}{}'.format(-i-1, what_module)]['bg'] = 'green'
                else:
                    globals()['state_ks4_51{}{}'.format(-i-1, what_module)]['bg'] = 'Red'

            globals()['P_in_1{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][30:32], 16)
            globals()['P_out_1{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][32:34], 16)
            globals()['P_mirrow_1{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][34:36], 16)
            globals()['P_in_2{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][48:50], 16)
            globals()['P_out_2{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][50:52], 16)
            globals()['P_mirrow_2{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][52:54], 16)
            globals()['P_in_3{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][66:68], 16)
            globals()['P_out_3{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][68:70], 16)
            globals()['P_mirrow_3{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][70:72], 16)
            globals()['P_in_4{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][84:86], 16)
            globals()['P_out_4{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][86:88], 16)
            globals()['P_mirrow_4{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][88:90], 16)
            globals()['code_fi_1{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][40:42], 16)
            globals()['code_fi_man_1{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][42:44], 16)
            globals()['code_fi_2{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][58:60], 16)
            globals()['code_fi_man_2{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][60:62], 16)
            globals()['code_fi_3{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][76:78], 16)
            globals()['code_fi_man_3{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][78:80], 16)
            globals()['code_fi_41{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][94:96], 16)
            globals()['code_fi_man_4{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][96:98], 16)
            globals()['code_att_1{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][44:46], 16)
            globals()['code_att_man_1{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][46:48], 16)
            globals()['code_att_2{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][62:64], 16)
            globals()['code_att_man_2{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][64:66], 16)
            globals()['code_att_3{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][80:82], 16)
            globals()['code_att_man_3{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][82:84], 16)
            globals()['code_att_4{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][98:100], 16)
            globals()['code_att_man_4{}'.format(what_module)]['text'] = int(opros.answers[int(what_module)][100:102],
                                                                            16)
        else:
            globals()['KS_1{}'.format(what_module)]['text'] = '(ノ º□º)ノ ⌒ ┴----┴'
            globals()['KS_2{}'.format(what_module)]['text'] = '¯\(°_0)/¯'
            globals()['KS_3{}'.format(what_module)]['text'] = 'обмена нет'
            globals()['KS_3{}'.format(what_module)]['fg'] = 'red'
        time.sleep(0.1)


if __name__ == '__main__':
    pass
