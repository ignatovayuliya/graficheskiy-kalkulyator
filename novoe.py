from tkinter import *
from tkinter import ttk
from random import choice #для замены цвета

root = Tk()
root.title('Графический калькулятор')

# меню с подменю
def callback():
    print ("Программа \"Графический калькулятор\" \nВыполнили: Осадчая Т.С., Игнатова Ю.А., группа 1652.")

def callback_again():
    print ('~~~Добро пожаловать в "Графический калькулятор!"~~~\n\n'
           'Пожалуйста, введите в поля ввода два числа, результаты математических операций\n'
           'с которыми Вы хотите узнать.\n'
           'Данная программа произведет расчет и выведет результат основных арифметических\n'
           'действий, а также возведения в степень и извлечения корня в графическом виде.\n')

menu = Menu(root)
root.config(menu=menu)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Инструкция", command=callback_again)
helpmenu.add_command(label="О программе", command=callback)

# параметры окошка
mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#ввод чисел   
chislo1 = StringVar()
chislo2 = StringVar()
chislo3 = StringVar()

text1 = ttk.Entry(mainframe, width=15, textvariable=chislo1)
text1.grid(column=2, row=2, sticky=(W, E))

text2 = ttk.Entry(mainframe, width=15, textvariable=chislo2)
text2.grid(column=2, row=5, sticky=(W, E))

# очистка полей
def ClearAll(*args):
    text1.delete(0,END)
    text2.delete(0,END)

# вызов окошка для выхода из программы
def Quit():
    root2 = Tk()
    root2.title('Выход')
    root2.geometry('200x150')
    mainframe2 = ttk.Frame(root2, padding='3 3 12 12')
    mainframe2.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe2.columnconfigure(0, weight=1)
    mainframe2.rowconfigure(0, weight=1)
    ttk.Label(mainframe2,  text='Вы действительно хотите выйти?').grid(column=1, row=1, sticky=(W, E))
    calculate_button = ttk.Button(mainframe2,  text='Да', command=mainframe2.quit)
    calculate_button.grid(column=1, row=3, sticky=(E))
    calculate_button = ttk.Button(mainframe2,  text='Нет', command=root2.destroy)
    calculate_button.grid(column=1, row=4, sticky=(E))

    # для расстояния между строчками и столбцами    
    for child in mainframe2.winfo_children():
        child.grid_configure(padx=10, pady=10)

# функция для вывода окна с основными арифметическими действиями
def calculate(*args):
    root3 = Tk()
    root3.title('Ваш пример')
    root3.geometry('330x320')
    mainframe3 = ttk.Frame(root3, padding='3 3 12 12')
    mainframe3.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe3.columnconfigure(0, weight=1)
    mainframe3.rowconfigure(0, weight=1)

    c = Canvas(mainframe3, width=300, height=300, bg="#D1FFD1")
    c.grid(row=0, column=0)

    colors = "Red Orange Yellow Green Blue Violet".split()
    c.pack(expand=1, fill=BOTH)
    
    # ф-я для замены цвета    
    def change(event):
        c.itemconfigure(CURRENT, fill=choice(colors))
 
    #рамка сверху
    oval1 = c.create_oval(10, 10, 40, 40, fill="white")
    treug1 = c.create_polygon([(70, 10), (40, 25), (70, 40)], fill="white")
    treug2 = c.create_polygon([(70, 10), (100, 25), (70, 40)], fill="white")
    hello = c.create_text((100, 20), text="Добро пожаловать!", anchor="nw")
    treug3 = c.create_polygon([(240, 10), (210, 25), (240, 40)], fill="white")
    treug4 = c.create_polygon([(240, 10), (270, 25), (240, 40)], fill="white")
    oval2 = c.create_oval(270, 10, 300, 40, fill="white")

    # проверка корректности и расчет по введенным данным
    try:
        value_1 = float(text1.get())
        value_2 = float(text2.get())
        chislo3_1 = '{0:.2f}'.format (float(value_1 + value_2))
        chislo3_2 = '{0:.2f}'.format (float(value_1 - value_2))
        chislo3_3 = '{0:.2f}'.format (float(value_1 * value_2))
        chislo3_4 = '{0:.2f}'.format (float(value_1 / value_2))
        chislo3_5 = '{0:.2f}'.format (float(value_1 ** value_2))
        chislo3_6 = '{0:.2f}'.format (float(value_1 ** (1/value_2)))

        #текст с результатами
        texx = c.create_text((30, 60), text=('Основные операции над данными числами:'),
                             anchor="nw", font=("Times", 10, 'bold', 'italic'))
        rez1 = c.create_text((40, 90), text=(value_1, '+', value_2, '=', chislo3_1), anchor="nw",
                             font=("Times", 10, 'italic'))
        rez2 = c.create_text((40, 120), text=(value_1, '-', value_2, '=', chislo3_2), anchor="nw",
                             font=("Times", 10, 'italic'))
        rez3 = c.create_text((40, 150), text=(value_1, '*', value_2, '=', chislo3_3), anchor="nw",
                             font=("Times", 10, 'italic'))
        rez4 = c.create_text((40, 180), text=(value_1, '/', value_2, '=', chislo3_4), anchor="nw",
                             font=("Times", 10, 'italic'))
        rez5 = c.create_text((40, 210), text=(value_1, '^', value_2, '=', chislo3_5), anchor="nw",
                             font=("Times", 10, 'italic'))
        rez6 = c.create_text((40, 240), text=(value_1, '√', value_2, '=', chislo3_6), anchor="nw",
                             font=("Times", 10, 'italic'))

        # расчет по введенным данным
        value_1 = float(text1.get())
        value_2 = float(text2.get())
        chislo3_1 = float(value_1 + value_2)
        chislo3_2 = float(value_1 - value_2)
        chislo3_3 = float(value_1 * value_2)
        chislo3_4 = float(value_1 / value_2)
        chislo3_5 = float(value_1 ** value_2)
        chislo3_6 = float(value_1 ** (1/value_2))

    # обработка исключений
    except ValueError:
        ttexx = c.create_text((60, 80), text=('Пожалуйста, введите числа'),
                             anchor="nw", font=("Times", 12, 'bold', 'italic'))
    except ZeroDivisionError:
        value_1 = float(text1.get())
        value_2 = float(text2.get())
        chislo3_1 = '{0:.2f}'.format (float(value_1 + value_2))
        chislo3_2 = '{0:.2f}'.format (float(value_1 - value_2))
        chislo3_3 = '{0:.2f}'.format (float(value_1 * value_2))
        chislo3_5 = '{0:.2f}'.format (float(value_1 ** value_2))

        #текст с результатами
        texx = c.create_text((30, 60), text=('Основные операции над данными числами:'),
                             anchor="nw", font=("Times", 10, 'bold', 'italic'))
        rez1 = c.create_text((40, 90), text=(value_1, '+', value_2, '=', chislo3_1), anchor="nw",
                             font=("Times", 10, 'italic'))
        rez2 = c.create_text((40, 120), text=(value_1, '-', value_2, '=', chislo3_2), anchor="nw",
                             font=("Times", 10, 'italic'))
        rez3 = c.create_text((40, 150), text=(value_1, '*', value_2, '=', chislo3_3), anchor="nw",
                             font=("Times", 10, 'italic'))
        rez4 = c.create_text((40, 180), text=('Деление на 0 запрещено!'), anchor="nw",
                             font=("Times", 10, 'italic'))
        rez5 = c.create_text((40, 210), text=(value_1, '^', value_2, '=', chislo3_5), anchor="nw",
                             font=("Times", 10, 'italic'))
        rez6 = c.create_text((40, 240), text=('Невозможно извлечь корень!'), anchor="nw",
                             font=("Times", 10, 'italic'))

        # расчет по введенным данным
        value_1 = float(text1.get())
        value_2 = float(text2.get())
        chislo3_1 = float(value_1 + value_2)
        chislo3_2 = float(value_1 - value_2)
        chislo3_3 = float(value_1 * value_2)
        chislo3_5 = float(value_1 ** value_2)

    #рамка снизу
    oval1_2 = c.create_oval(10, 270, 40, 300, fill="white")
    treug1_2 = c.create_polygon([(70, 270), (40, 285), (70, 300)], fill="white")
    treug2_2 = c.create_polygon([(70, 270), (100, 285), (70, 300)], fill="white")
    kvadr2 = c.create_rectangle(210, 290, "100", "280", fill="white")
    treug3_2 = c.create_polygon([(240, 270), (210, 285), (240, 300)], fill="white")
    treug4_2 = c.create_polygon([(240, 270), (270, 285), (240, 300)], fill="white")
    oval2_2 = c.create_oval(270, 270, 300, 300, fill="white")

    #смена цвета фигур по щелчку
    c.tag_bind(oval1, "<1>", change)
    c.tag_bind(treug1, "<1>", change)
    c.tag_bind(treug2, "<1>", change)
    c.tag_bind(treug3, "<1>", change)
    c.tag_bind(treug4, "<1>", change)
    c.tag_bind(oval2, "<1>", change)
    c.tag_bind(oval1_2, "<1>", change)
    c.tag_bind(treug1_2, "<1>", change)
    c.tag_bind(treug2_2, "<1>", change)
    c.tag_bind(kvadr2, "<1>", change)
    c.tag_bind(treug3_2, "<1>", change)
    c.tag_bind(treug4_2, "<1>", change)
    c.tag_bind(oval2_2, "<1>", change)
    
    c.pack()
     
    # для расстояния между строчками и столбцами 
    for child in mainframe3.winfo_children():
        child.grid_configure(padx=10, pady=5)
    
# кнопочки    
calculate_button = ttk.Button(mainframe,  text='Рассчитать', command=calculate)
calculate_button.grid(column=4, row=6, sticky=(W, E))

calculate_button = ttk.Button(mainframe,  text='Очистить', command=ClearAll)
calculate_button.grid(column=2, row=6, sticky=(E))

calculate_button = ttk.Button(mainframe,  text='Выход', command=Quit)
calculate_button.grid(column=3, row=7, sticky=(W, E))

# метки с подсказками
ttk.Label(mainframe,  text='Первое число').grid(column=3, row=2, sticky=(W))
ttk.Label(mainframe,  text='Второе число').grid(column=3, row=5, sticky=(W))

# для расстояния между строчками и столбцами 
for child in mainframe.winfo_children():
    child.grid_configure(padx=10, pady=10)

# помещает курсор в первое поле для ввода
text1.focus()

# вывод результата расчета также по щелчку на кнопку Enter
root.bind('<Return>', calculate)

root.mainloop()
