"""
На пространстве формы изображен календарь за март текущего года
с горизонтальным расположением недель. Дни недели подписаны.
Метка в виде окружности циклически движется в обратном направлении
по датам, начиная с последней, с дискретом 0.6 сек. Запуск движения
– кнопка «Пуск», остановка – команда главного меню, что приводит
к установке рамки на последнюю дату.
"""

from tkinter import *
from time import *
root = Tk()
root.geometry('500x410')
root.resizable(0,0)
root.title('Богданов Максим 19-ИЭ-1')
c = Canvas(width = 500, height = 410, bg = 'grey')
c.pack()

flag = 0

def evStart(event):
    global flag
    btnStart.place_forget()
    c.delete('ramka')
    flag = 1
    work()

def work():
    global X, Y, flag, Xr, Yr
    dop = 0
    for i in range(32):
        sleep(0.6)
        if flag == 1:
            
            c.create_oval(X,Y,X+50,Y+50, tag = 'oval', outline = 'red', width = 2)
            Xr = X
            Yr = Y
            if i+1 == 3:
                Y -= 50
                X += 420
                
            if i+1 == 10:
                Y -= 50
                X += 420
                
            if i+1 == 17:
                Y -= 50
                X += 420
                
            if i+1 == 24:
                Y -= 50
                X += 420
  
            X -= 60
            dop += 1 
            c.update()
            
        elif flag == 0:
            X = 165 
            Y = 250
            return 0
        c.delete('oval')
        
        if dop == 31:
            X = 165 
            Y = 250
            work()

def evStop(*args):
    global flag, Xr, Yr
    c.create_oval(Xr,Yr,Xr+50,Yr+50, tag = 'ramka', outline = 'red', width = 2)
    btnStart.place(x = 120, y = 325)
    flag = 0

Y = 80
X = 10

for i in range(31): # Создание чисел
    X += 60
    c.create_text(X,Y,text = i+1, fill = 'white', font = 'Verdana 30')
    c.create_line(X-1000,Y+20,X+1000,Y+20)
    if i+1 == 7:
        c.create_line(X-1000, Y - 30, X + 100, Y - 30)
        Y += 50
        X -= 420

    if  i+1 == 14:
        Y += 50
        X -= 420

    if  i+1 == 21:
        Y += 50
        X -= 420

    if  i+1 == 28:
        Y += 50
        X -= 420

    if  i+1 == 31:
        Y += 50
        X -= 420

Y = 80
X = 10

dni = ['ПН','ВТ','СР','ЧТ','ПТ','СБ','ВС','']
for i in range(8):
    X += 60
    c.create_text(X,Y-50, text = dni[i], font = 'Verdana 30', fill = 'red')
    c.create_line(X-30,Y-150,X-30,Y+220)

btnStart = Button(text = 'Пуск', font = "Verdana 12", width = 20, height = 1, bg = 'lightgreen')
btnStart.place(x = 150, y = 325)
btnStart.bind('<ButtonRelease-1>', evStart)

mainMenu = Menu(root)
root.config(menu = mainMenu)
Menu.add_command(mainMenu, label = "Стоп", command = evStop)

X = 165
Y = 250
Xr = 0 #переменные, необходимые для того, чтобы 
Yr = 0 #запомнить последнее положение рамки

root.mainloop()
