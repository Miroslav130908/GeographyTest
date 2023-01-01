from tkinter import *
import time
import random


irus1 = 0
rus1ques = ['А?', 'Б?', 'В?']


def rus1d():
    def rus1quit():
        global irus1
        irus1 = 0
        rus1.destroy()

    def rus1go():
        global irus1
        rus1que.config(text=rus1ques[irus1])
        if irus1 < len(rus1ques) - 1:
            irus1 += 1
        else:
            rus1que.config(text='Конец!')
            rus1ans1.config(text='Закрыть', command=rus1quit)
    rus1 = Toplevel()
    rus1.title('Тест по рельефу')
    rus1.geometry('1400x1000')

    rus1qus = Frame(rus1)
    rus1pic = Frame(rus1)
    rus1que = Label(rus1qus, text='Начать тест?', bg='black', fg='white', font='Arial, 30', width=56, height=1)
    rus1ans1 = Button(rus1qus, text='Да', command=rus1go, bg='black', fg='white')
    rus1can = Canvas(rus1pic, height=884, width=1400)

    rus1map = PhotoImage(file='MapMountainsAndPlains1.png')
    rus1can.create_image(0, 0, anchor=NW, image=rus1map)

    rus1qus.grid(row=0)
    rus1pic.grid(row=1)
    rus1que.grid(row=0, column=0)
    rus1ans1.grid(row=1, column=0)
    rus1can.grid(row=0, column=0)
    rus1.mainloop()


root = Tk()
root.title('Сборник тестов по географии')
root.geometry('1400x800')
rus1but = Button(root, text='Рельеф России карта', command=rus1d, bg='black', fg='white', font='Arial, 30', width=18, height=1)
rus1but.grid(row=0, column=0)
root.mainloop()
