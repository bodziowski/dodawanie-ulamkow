from tkinter import *
from tkinter.ttk import Combobox
from PIL import ImageTk,Image 
import tkinter.messagebox as msb
licznikliczby1=[]
mianownikliczby1 = []
liczbaokien = 0
liczbanr = 1
czysaliczby = 0
oknoglowne = Tk()
oknoglowne.geometry("300x300")
oknoglowne.title("Kalkulator")
def start():
    print(wybor.get())
    global wybor2
    wybor2 = wybor.get()
    wybor.pack_forget()
    okno()
wybor = Combobox(oknoglowne)
wybor['values']=["DODAWANIE","ODEJMOWANIE"]
wybor.pack(fill=BOTH)
wybor.current(0)
licz = Button(text="dodaj liczby",command=start)
licz.pack(fill=BOTH)
canvas = Canvas(oknoglowne, width = 0, height = 200)     
canvas.pack(fill=BOTH)
obraz = ImageTk.PhotoImage(Image.open("ul.jpg"))    
canvas.create_image(20,20, anchor=NW, image=obraz)
def okno():
    def wezliczbe():
        global liczbaokien
        global licz
        global liczbanr
        global licznikliczby1
        global wybor
        global czysaliczby
        if wejscie1.get()=="" or wejscie2.get()=="":
            msb.showinfo("problem", "dodaj poprawne liczby")
            liczbaokien = 0
            oknoentry.destroy()
            licz.pack(fill=BOTH)
            #zamyka funkcje
            return 0
        wejscielicznika1 = wejscie1.get()
        licznikliczby1.append(wejscielicznika1)
        global mianownikbliczby1
        wejsciemianownika1 = wejscie2.get()
        mianownikliczby1.append(wejsciemianownika1)
        msb.showinfo("Info", "pomyślnie dodoano liczbe nr." + str(liczbanr))
        wejscie1.delete(0,"end")
        wejscie2.delete(0,"end")
        if liczbanr == 2:
            oknoentry.destroy()
            liczbaokien-=1
            licz.pack(fill=BOTH)
            liczbanr = 0
            if wybor.get()=="DODAWANIE":
                czysaliczby +=1
                test()
        liczbanr = int(liczbanr) +1
    global licz
    global liczbaokien
    global oknoentry
    if liczbaokien == 1:
        msb.showinfo("PROBLEM", "Zamknij pozostałe okna!")
    elif liczbaokien == 2:
        msb.showinfo("PROBLEM", "Zamknij pozostałe okna!")
    else:
        licz.pack_forget()
        liczbaokien+=1
        oknoentry = Tk()
        oknoentry.geometry("100x100")
        wejscie1 = Entry(oknoentry)
        wejscie1.pack(fill=BOTH)
        text1 = Label(oknoentry,text="podaj licznik^")
        text1.pack(fill=BOTH)
        wejscie2 = Entry(oknoentry)
        wejscie2.pack(fill=BOTH)
        text1 = Label(oknoentry,text="podaj mianownik^")
        text1.pack(fill=BOTH)
        button1 = Button(oknoentry,text="dalej",command=wezliczbe).pack(fill=BOTH)
        def zamk():
            global liczbaokien
            print("LUL")
            licz.pack(fill=BOTH)
            oknoentry.destroy()
            liczbaokien = 0
        oknoentry.protocol("WM_DELETE_WINDOW",zamk)
        oknoentry.mainloop()
def test():
    global czysaliczby
    global liczbanr
    global licznikliczby1
    global mianownikliczby1
    global wynik3
    global wynikcaly
    global licznikliczby1
    global mianownikliczby1
    lliczby1 = licznikliczby1[0]
    mliczby1 = mianownikliczby1[0]
    lliczby2 = licznikliczby1[1]
    mliczby2 = mianownikliczby1[1]
    wynik1 = int(lliczby1) * int(mliczby2)
    wynik2 = int(mliczby1) * int(lliczby2)
    wynik3 = int(mliczby1) * int(mliczby2)
    wynikcaly = int(wynik1)+int(wynik2)
    while wynik3 %2== 0 and wynikcaly%2==0:
        wynik3/=2
        wynikcaly/=2
        print("liczba2",wynik3)
        print("liczba2",wynikcaly)
        if wynik3 <= 2 or wynikcaly <= 2 :
            break
        else:
            continue
    while wynik3 %3== 0 and wynikcaly%3==0:
        wynik3/=3
        wynikcaly/=3
        print("liczba3",wynik3)
        print("liczba3",wynikcaly)
        if wynik3 <= 3 or wynikcaly <= 3:
            break
        else:
            continue
    while wynik3 %5== 0 and wynikcaly%5==0:
        wynik3/=5
        wynikcaly/=5
        print("liczba5",wynik3)
        print("liczba5",wynikcaly)
        if wynik3 <= 5 or wynikcaly <= 5:
            break
        else:
            continue
    while wynik3 %7== 0 and wynikcaly%7==0:
        wynik3/=7
        wynikcaly/=7
        print("liczba",wynik3)
        print("liczba7",wynikcaly)
        if wynik3 == 7 or wynikcaly == 7:
            break
        else:
            continue
    mianownikliczby1 = []
    licznikliczby1 = []
    liczbanr = 0
def wynik():
    global czysaliczby
    global oknowynik
    global liczbaokien
    global wynikcaly
    global wynik3
    if liczbanr==0:
        return 0 
    oknowynik = Tk()
    oknowynik.geometry("200x200")
    oknowynik.title("wynik")
    tekstwynik = Label(oknowynik,text="licznik to  "+str(wynikcaly)+" mianownik to "+str(wynik3))
    tekstwynik.pack(fill=BOTH,expand=YES)
    global licznikliczby1
    global mianownikliczby1
    mianownikliczby1 = []
    licznikliczby1 = []
    liczbaokien = 0
    print(liczbaokien)
    oknowynik.mainloop()
policzliczby=Button(text="policz",command=wynik).pack(fill=BOTH)
def gh():
    #print("LUL")
    try:
        oknoglowne.destroy()
    except:
        ()
    try:
        oknoentry.destroy()
    except:
        ()
    try:
        oknowynik.destroy()
    except:
        ()
oknoglowne.protocol("WM_DELETE_WINDOW",gh)
oknoglowne.mainloop()