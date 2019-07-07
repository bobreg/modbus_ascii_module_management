import tkinter
import opros
import super_puper_proga
import threading


def configure_program():
    opros.choise_start = choise_start.get()
    opros.find_port()
    threading.Thread(opros.find_module()).start()
    starting_window.destroy()
    super_puper_proga

starting_window = tkinter.Tk()
starting_window.title('Старт')

choise_start = tkinter.IntVar()

text_label = tkinter.Label(starting_window, text='Выберите параметр\nзапуска программы', font='Arial 12', anchor='center')
radiobutton_old_find = tkinter.Radiobutton(starting_window, text='поиск модулей по\nкомандам 51, 49, 47', value=1, variable=choise_start)
radiobutton_ID_find = tkinter.Radiobutton(starting_window, text='поиск модулей по ID', value=2, variable=choise_start)
radiobutton_old_configure = tkinter.Radiobutton(starting_window, text='загрузить последнюю\nконфигурацию', value=3, variable=choise_start)
start_button = tkinter.Button(starting_window, text='Старт', command=configure_program)

text_label.place(x=20, y=10)
radiobutton_old_find.place(x=10, y=60)
radiobutton_ID_find.place(x=10, y=100)
radiobutton_old_configure.place(x=10, y=130)
start_button.place(x=80, y=180)


starting_window.geometry('200x220+300+300')
starting_window.mainloop()
