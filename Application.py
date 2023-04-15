from tkinter import *
import time
import random
import json
from PIL import Image, ImageTk


rans = 0
i = 0
fontind = None
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



def rootd(f):
    def rootdi():
        global data, imagename, fontind
        with open(f'data/test{f}.json', encoding='utf-8') as file:
            data = json.load(file)
            fontind = f
        imagename = f'data/test{f}.png'
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
    
    
        
    def sliceandice():
        global i, rans
        i = 0
        rans = 0
        rus.destroy()


    def check():
        global rans
        global ans
        global i
        if i < len(ind) - 1:
            if ans == data[ind[i]]['cors']:
                rans += 1
                cind['text'] = 'Верно!'
                cind['bg'] = 'green'
                megarind.create_oval((15 * smx) / 30 * (2 * i + 1) - smy / 4, smy / 2 + smy / 4, (15 * smx) / 30 * (2 * i + 1) + smy / 4, smy / 2 - smy / 4, fill='green', outline='green')
            else:
                cind['text'] = 'Неверно!'
                cind['bg'] = 'red'
                megarind.create_oval((15 * smx) / 30 * (2 * i + 1) - smy / 4, smy / 2 + smy / 4, (15 * smx) / 30 * (2 * i + 1) + smy / 4, smy / 2 - smy / 4, fill='red', outline='red')
            i += 1
            que['text'] = data[ind[i]]['ques']
            for j in range(len(data[0]['anss'])):
                buts[j]['text'] = data[ind[i]]['anss'][j]
            rind['text'] = f'Верно: {rans} / {i}'
        else:
            if ans == data[ind[i]]['cors']:
                rans += 1
                cind['text'] = 'Верно!'
                cind['bg'] = '#9190d6'
                megarind.create_oval((15 * smx) / 30 * (2 * i + 1) - smy / 4, smy / 2 + smy / 4, (15 * smx) / 30 * (2 * i + 1) + smy / 4, smy / 2 - smy / 4, fill='green', outline='green')
            else:
                cind['text'] = 'Неверно!'
                cind['bg'] = 'yellow'
                megarind.create_oval((15 * smx) / 30 * (2 * i + 1) - smy / 4, smy / 2 + smy / 4, (15 * smx) / 30 * (2 * i + 1) + smy / 4, smy / 2 - smy / 4, fill='red', outline='red')
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
            for k in range(len(data[0]['anss'])):
                buts[k]['command'] = end
            i = 0
            rans = 0


    rus = Toplevel()
    rus.title('Тест по рельефу')
    # rus.geometry('1400x1000')tf
    rus.attributes('-fullscreen', True)
    
    if fontind == 1 or fontind == 3 or fontind == 5 or fontind == 6 or fontind == 9 or fontind == 10:
        tfont = f'Arial, {35 if sx >= 2500 and sy >= 1200 else 25 if sx >= 1400 and sy >= 800 else 15}'
    if fontind == 2 or fontind == 4 or fontind == 7 or fontind == 8:
        tfont = f'Arial, {25 if sx >= 2500 and sy >= 1200 else 15 if sx >= 1400 and sy >= 800 else 10}'
    else:
        tfont = f'Arial, {30 if sx >= 2500 and sy >= 1200 else 20 if sx >= 1400 and sy >= 800 else 13}'
    
    tmy = sy / 14
    tmx = sx / 7
    
    que = Label(rus, text=data[ind[0]]['ques'], bg='black', fg='white', font=tfont, width=67, height=1)
    buts = []
    for j in range(len(data[0]['anss'])):
        buts.append(Button(rus, text=data[ind[0]]['anss'][j], command=butcc(j), bg='black', fg='white', font=tfont, wraplength=(tmx - 10)))
    cind = Label(rus, text='-------', bg='black', fg='white', font=tfont, width=15, height=1)
    rind = Label(rus, text='Верно: 0 / 0', bg='yellow', fg='black', font=tfont, width=15, height=1)
    megarind = Canvas(rus)
    smx = 0.3 * tmx
    smy = tmy
    for j in range(15):
        megarind.create_oval((15 * smx) / 30 * (2 * j + 1) - smy / 4, smy / 2 + smy / 4, (15 * smx) / 30 * (2 * j + 1) + smy / 4, smy / 2 - smy / 4, fill='#7f8584', outline='#7f8584')
    slice = Button(rus, text='←', bg='black', fg='#5694db', activeforeground='black', activebackground='#5694db', font=rfont, command=sliceandice)


    mapx = Image.open(imagename)
    mapx = mapx.resize(((sx - sx // 7), (sy - sy // 7)), Image.ANTIALIAS)
    map = ImageTk.PhotoImage(mapx)
    maplab = Label(rus, image=map)
    
    
    maplab.place(x=0, y=(sy / 7))
    for j in range(len(data[0]['anss'])):
        buts[j].place(x=(tmx * 6), y=(tmy * 2 + j * 2 * tmy + tmy / 4), width=tmx, height=(tmy + tmy / 2))
    que.place(x=0, y=0, width=(tmx * 7), height=tmy)
    rind.place(x=0, y=tmy, width=(tmx * 1.5), height=tmy)
    cind.place(x=(tmx * 6), y=tmy, width=(tmx * 1), height=tmy)
    megarind.place(x=(tmx * 1.5), y=tmy, width=(tmx * 4.5), height=tmy)
    slice.place(x=0, y=0, width=(sx / 30), height=(sy / 30))
    
    
    rus.mainloop()


def dashanddestroy():
    root.destroy()



root = Tk()
root.title('Сборник тестов по географии')
# root.geometry('1400x800')
root.attributes('-fullscreen', True)
sx = root.winfo_screenwidth()
sy = root.winfo_screenheight()


rootbgx = Image.open("Backgroundroot.png")
rootbgx = rootbgx.resize((sx, sy), Image.LANCZOS)
rootbg = ImageTk.PhotoImage(rootbgx)
rootbglab = Label(root, image=rootbg)
rootbglab.place(x=0, y=0, relwidth=1, relheight=1)

rmx = sx // 16
rmy = sy // 24
rfont = f'Arial, {40 if sx >= 2500 and sy >= 1200 else 30 if sx >= 1400 and sy >= 800 else 20}'
names = ['Горы и равнины России I', 'Горы и равнины России II', 'Моря, заливы, проливы РФ', 'Острова и полуострова РФ',
         'Реки России', 'Озера и губы России', 'Реки России II', 'Озера и губы России II',
         'Города России', 'Границы России']
for j in range(10):
    but = Button(root, text=names[j], command=rootd((j % 10) + 1), bg='black', fg='white', font=rfont)
    but.place(x=(rmx + (j // 5) * rmx * 8), y=(5 * rmy + (j % 5) * rmy * 4), width=(6 * rmx), height=(2 * rmy))
rootname = Label(root, text='Сборник тестов по географии. Выберите тест:', bg='black', fg='white', font=rfont)
dash = Button(root, text='×', bg='black', fg='red', activeforeground='black', activebackground='red', font=rfont, command=dashanddestroy)
rootname.place(x=rmx, y=rmy, width=(14 * rmx), height=(2 * rmy))
dash.place(x=(sx - sx / 30), y=0,  width=(sx / 30), height=(sy / 30))
root.mainloop()
