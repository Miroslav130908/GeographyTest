from tkinter import *
import time
import random
from tkinter.messagebox import *

rus1rans = 0
irus1 = 0
rus1ques = ['Какой цифрой на карте обозначен Буреинский хребет?', 'Какой цифрой на карте обозначены Уральские горы?', 'Какой цифрой на карте обозначено плато Путорана?', 'Какой цифрой на карте обозначена Среднерусская возвышенность?', 'Какой цифрой на карте обозначено Западно-Сибирское плоскогорье?', 'Какой цифрой на карте обозначен хребет Джугджур?', 'Какой цифрой на карте обозначено Патомское нагорье?', 'Какой цифрой на карте обозначен Верхоянский хребет?', 'Какой цифрой на карте обозначено Алданское нагорье?', 'Какой цифрой на карте обозначены Кавказские горы?', 'Какой цифрой на карте обозначен хребет Черского?', 'Какой цифрой на карте обозначен Восточный Саян?', 'Какой цифрой на карте обозначены Хибины?', 'Какой цифрой на карте обозначено Чукотское нагорье?', 'Какой цифрой на карте обозначено Становое нагорье?', 'Какой цифрой на карте обозначены горы Бырранга?', 'Какой цифрой на карте обозначен Яблоновый хребет?', 'Какой цифрой на карте обозначен Сихотэ-Алинь?', 'Какой цифрой на карте обозначен Алтай?', 'Какой цифрой на карте обозначен Срединный хребет?']
rus1ans1s = ['11', '12', '10', '4', '12', '3', '14', '4', '18', '3', '10', '6', '5', '5', '10', '4', '6', '7', '5', '13']
rus1ans2s = ['9', '5', '19', '10', '17', '20', '19', '18', '12', '14', '19', '7', '11', '12', '13', '11', '17', '8', '7', '19']
rus1ans3s = ['1', '4', '13', '19', '10', '7', '2', '9', '19', '12', '4', '15', '18', '16', '20', '14', '2', '12', '14', '8']
rus1ans4s = ['19', '3', '15', '8', '7', '1', '17', '16', '15', '7', '3', '17', '8', '8', '8', '9', '10', '4', '11', '16']
rus1ans5s = ['2', '9', '2', '16', '13', '11', '18', '3', '10', '5', '20', '1', '20', '20', '15', '5', '7', '5', '9', '4']
rus1ans6s = ['3', '10', '17', '12', '19', '5', '4', '11', '5', '19', '8', '9', '14', '6', '16', '6', '19', '1', '18', '2']
rus1cors = [5, 4, 3, 2, 1, 3, 4, 3, 1, 5, 2, 3, 4, 5, 6, 2, 1, 6, 3, 5]


def saysth(title, text, ind):
    def closesss():
        sss.destroy()

    sss = Toplevel()
    sss.title(title)
    if ind == 0:
        sss['bg'] = 'red'
    if ind == 1:
        sss['bg'] = 'green'
    if ind == 2:
        sss['bg'] = 'blue'
    ssslabel = Label(sss, text=text, font='Arial, 20', height=1, bg='#e0ded7')
    sssbutton = Button(sss, text='  ОК  ', font='Arial, 20', height=1, bg='#e0ded7', command=closesss)

    ssslabel.grid(row=0)
    sssbutton.grid(row=1)


def rus1d():
    global rus1rans
    global irus1
    rus1ans = 0
    indrus1 = [x for x in range(20)]
    random.shuffle(indrus1)
    indrus1 = indrus1[:-5]

    def rus1but1c():
        global rus1ans
        rus1ans = 1
        rus1check()

    def rus1but2c():
        global rus1ans
        rus1ans = 2
        rus1check()

    def rus1but3c():
        global rus1ans
        rus1ans = 3
        rus1check()

    def rus1but4c():
        global rus1ans
        rus1ans = 4
        rus1check()

    def rus1but5c():
        global rus1ans
        rus1ans = 5
        rus1check()

    def rus1but6c():
        global rus1ans
        rus1ans = 6
        rus1check()


    def rus1check():
        global rus1rans
        global rus1ans
        global irus1
        if irus1 < len(indrus1) - 1:
            if rus1ans == rus1cors[indrus1[irus1]]:
                irus1 += 1
                saysth('Верно!', 'Следующий вопрос!', 1)
                rus1que['text'] = rus1ques[indrus1[irus1]]
                rus1ans1['text'] = rus1ans1s[indrus1[irus1]]
                rus1ans2['text'] = rus1ans2s[indrus1[irus1]]
                rus1ans3['text'] = rus1ans3s[indrus1[irus1]]
                rus1ans4['text'] = rus1ans4s[indrus1[irus1]]
                rus1ans5['text'] = rus1ans5s[indrus1[irus1]]
                rus1ans6['text'] = rus1ans6s[indrus1[irus1]]
                rus1rans += 1
            else:
                irus1 += 1
                saysth('Неверно!', 'Следующий вопрос...', 0)
                rus1que['text'] = rus1ques[indrus1[irus1]]
                rus1ans1['text'] = rus1ans1s[indrus1[irus1]]
                rus1ans2['text'] = rus1ans2s[indrus1[irus1]]
                rus1ans3['text'] = rus1ans3s[indrus1[irus1]]
                rus1ans4['text'] = rus1ans4s[indrus1[irus1]]
                rus1ans5['text'] = rus1ans5s[indrus1[irus1]]
                rus1ans6['text'] = rus1ans6s[indrus1[irus1]]
        else:
            if rus1ans == rus1cors[indrus1[irus1]]:
                saysth('Конец!', 'Верно, ты прошёл тест!', 2)
                rus1rans += 1
                rus1result = 'Твой результат: ' + str(rus1rans) + ' / 15'
                rus1que['text'] = rus1result
            else:
                saysth('Конец!', 'Неверно, но ты прошёл тест!', 2)
                rus1result = 'Твой результат: ' + str(rus1rans) + ' / 15'
                rus1que['text'] = rus1result


    rus1 = Toplevel()
    rus1.title('Тест по рельефу')
    rus1.geometry('1400x1000')

    rus1qus = Frame(rus1)
    rus1pic = Frame(rus1)
    rus1que = Label(rus1qus, text=rus1ques[indrus1[0]], bg='black', fg='white', font='Arial, 25', width=67, height=1)
    rus1ans1 = Button(rus1qus, text=rus1ans1s[indrus1[0]], command=rus1but1c, bg='black', fg='white', font='Arial, 30', width=10, height=1)
    rus1ans2 = Button(rus1qus, text=rus1ans2s[indrus1[0]], command=rus1but2c, bg='black', fg='white', font='Arial, 30', width=10, height=1)
    rus1ans3 = Button(rus1qus, text=rus1ans3s[indrus1[0]], command=rus1but3c, bg='black', fg='white', font='Arial, 30', width=10, height=1)
    rus1ans4 = Button(rus1qus, text=rus1ans4s[indrus1[0]], command=rus1but4c, bg='black', fg='white', font='Arial, 30', width=10, height=1)
    rus1ans5 = Button(rus1qus, text=rus1ans5s[indrus1[0]], command=rus1but5c, bg='black', fg='white', font='Arial, 30', width=10, height=1)
    rus1ans6 = Button(rus1qus, text=rus1ans6s[indrus1[0]], command=rus1but6c, bg='black', fg='white', font='Arial, 30', width=10, height=1)
    rus1can = Canvas(rus1pic, height=884, width=1400)

    rus1map = PhotoImage(file='MapMountainsAndPlains1.png')
    rus1can.create_image(0, 0, anchor=NW, image=rus1map)

    rus1qus.grid(row=0)
    rus1pic.grid(row=1)
    rus1que.grid(row=0, columnspan=3, column=0)
    rus1ans1.grid(row=1, column=0)
    rus1ans2.grid(row=1, column=1)
    rus1ans3.grid(row=1, column=2)
    rus1ans4.grid(row=2, column=0)
    rus1ans5.grid(row=2, column=1)
    rus1ans6.grid(row=2, column=2)
    rus1can.grid(row=0, column=0)
    rus1.mainloop()


root = Tk()
root.title('Сборник тестов по географии')
root.geometry('1400x800')
rus1but = Button(root, text='Рельеф России карта', command=rus1d, bg='black', fg='white', font='Arial, 30', width=18, height=1)
rus1but.grid(row=0, column=0)
root.mainloop()
