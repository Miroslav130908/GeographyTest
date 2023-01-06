from tkinter import *
import time
import random
import json


rans = 0
i = 0

ans = -1
data = None
imagename = None


# with open('data/test1.json') as file:
#     tmp = json.load(file)


# with open('data/test1.json', 'w') as file:
#     json.dump(res, file, sort_keys=False, indent=4, ensure_ascii=False)


def saysth(title, text, ind):
    bg = 'white'
    def closesss():
        sss.destroy()

    sss = Tk()
    sss.title(title)
    sss.eval('tk::PlaceWindow . center')
    sss['bg'] = '#e0ded7'
    if ind == 0:
        bg = 'red'
    if ind == 1:
        bg = 'green'
    if ind == 2:
        bg = '#9190d6'
    ssslabel = Label(sss, text=text, font='Arial, 20', height=1, width=20, bg=bg)
    sssbutton = Button(sss, text='  ОК  ', font='Arial, 20', height=1, bg='#e0ded7', command=closesss)

    ssslabel.grid(row=0)
    sssbutton.grid(row=1)


def rootd(i):
    def rootdi():
        global data, imagename
        with open(f'data/test{i}.json') as file:
            data = json.load(file)
        imagename = f'data/test{i}.png'
        d()
    return rootdi


def d():
    global rans
    global i
    ind = [x for x in range(20)]
    random.shuffle(ind)
    ind = ind[:-5]

    def butcc(i):
        def butc():
            global ans
            ans = i
            check()
        return butc


    def end():
        saysth('Конец', 'Тест уже закончился!', 2)


    def check():
        global rans
        global ans
        global i
        if i < len(ind) - 1:
            if ans == data[ind[i]]['cors']:
                rans += 1
                cind['text'] = 'Верно!'
                cind['bg'] = 'green'
            else:
                cind['text'] = 'Неверно!'
                cind['bg'] = 'red'
            i += 1
            que['text'] = data[ind[i]]['ques']
            for j in range(6):
                buts[j]['text'] = data[ind[i]]['anss'][j]
            rind['text'] = f'Верно: {rans} / {i}'
        else:
            if ans == data[ind[i]]['cors']:
                rans += 1
                cind['text'] = 'Верно! Конец!'
                cind['bg'] = '#9190d6'
            else:
                cind['text'] = 'Неверно! Конец!'
                cind['bg'] = 'yellow'
            if rans > 12:
                oc = rans - 10
            if rans == 12:
                oc = 3
            if rans < 12 and rans > 9:
                oc = 2
            if rans <= 9:
                oc = 1
            que['text'] = f'Твой результат: {rans} / 15, Оценка: {oc}'
            cind['fg'] = 'black'
            rind['text'] = f'Верно: {rans} / {i + 1}'
            for k in range(6):
                buts[k]['command'] = end
            i = 0
            rans = 0


    rus = Toplevel()
    rus.title('Тест по рельефу')
    rus.geometry('1400x1000')


    qus = Frame(rus)
    qus['bg'] = '#87e88a'
    pic = Frame(rus)
    que = Label(qus, text=data[ind[0]]['ques'], bg='black', fg='white', font='Arial, 25', width=67, height=1)
    buts = []
    for j in range(6):
        buts.append(Button(qus, text=data[ind[0]]['anss'][j], command=butcc(j), bg='black', fg='white', font='Arial, 30', width=10, height=1))
    cind = Label(qus, text='Выберите ответ', bg='black', fg='white', font='Arial, 25', width=15, height=1)
    rind = Label(qus, text='Верно: 0 / 0', bg='yellow', fg='black', font='Arial, 25', width=15, height=1)
    can = Canvas(pic, height=884, width=1400)

    map = PhotoImage(file=imagename)
    can.create_image(0, 0, anchor=NW, image=map)

    qus.grid(row=0)
    pic.grid(row=1)
    que.grid(row=0, columnspan=4, column=0)
    for j in range(6):
        buts[j].grid(row=(1 + j // 3), column=(j % 3))
    rind.grid(row=1, column=3)
    can.grid(row=2, column=3)
    cind.grid(row=2, column=3)
    rus.mainloop()


root = Tk()
root.title('Сборник тестов по географии')
root.geometry('1400x800')

rootbg = PhotoImage(file='Backgroundroot.png')
rootbglab = Label(root, image=rootbg)
rootbglab.place(x=0, y=0, relwidth=1, relheight=1)

but = Button(root, text='Горы и равнины России', command=rootd(1), bg='black', fg='white', font='Arial, 30', width=25, height=1)
but.grid(row=0, column=0)
root.mainloop()
