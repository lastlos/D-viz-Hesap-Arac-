import tkinter
from bs4 import BeautifulSoup
import requests
from tkinter import *
from tkinter import ttk

class arayuz:

    def __init__(self, window):

        girdi1 = StringVar()

        def press0():
            num1 = float(girdi1.get())
            girdi = num1
            url = "https://dolar.tlkur.com/"
            result = requests.get(url)
            doc = BeautifulSoup(result.text, "html.parser")
            dolar_tl = doc.find_all(id="USDTRY")  # Dosyada (sitede) arama yapar.
            dolar_tl_parent = dolar_tl[0].parent
            dolar_tl_span = dolar_tl_parent.find("span")
            dolar_tl_kur = dolar_tl_span.string
            kur0 = float(dolar_tl_kur)
            sonuc = girdi * kur0
            global label0
            label0 = Label(window, text=sonuc, bg="grey", fg="white")
            label0["font"] = ("Futura", 20)
            label0.pack()


        def press1():
            num1 = float(girdi1.get())
            girdi = num1
            url = "https://dolar.tlkur.com/"
            result = requests.get(url)
            doc = BeautifulSoup(result.text, "html.parser")
            dolar_tl = doc.find_all(id="USDTRY")  # Dosyada (sitede) arama yapar.
            dolar_tl_parent = dolar_tl[0].parent
            dolar_tl_span = dolar_tl_parent.find("span")
            dolar_tl_kur = dolar_tl_span.string
            kur0 = float(dolar_tl_kur)
            sonuc = girdi / kur0

            global label1
            label1 = Label(window, text=sonuc, bg="grey", fg="white")

            label1["font"] = ("Futura", 20)
            label1.pack()

        def press2():
            num1 = float(girdi1.get())
            girdi = num1
            url = "https://dolar.tlkur.com/"
            result = requests.get(url)
            doc = BeautifulSoup(result.text, "html.parser")
            dolar_tl = doc.find_all(id="EURTRY")  # Dosyada (sitede) arama yapar.
            dolar_tl_parent = dolar_tl[0].parent
            dolar_tl_span = dolar_tl_parent.find("span")
            dolar_tl_kur = dolar_tl_span.string
            kur0 = float(dolar_tl_kur)
            sonuc = girdi * kur0

            global label2
            label2 = Label(window, text=sonuc, bg="grey", fg="white")
            label2["font"] = ("Futura", 20)
            label2.pack()

        def press3():
            num1 = float(girdi1.get())
            girdi = num1
            url = "https://dolar.tlkur.com/"
            result = requests.get(url)
            doc = BeautifulSoup(result.text, "html.parser")
            dolar_tl = doc.find_all(id="EURTRY")  # Dosyada (sitede) arama yapar.
            dolar_tl_parent = dolar_tl[0].parent
            dolar_tl_span = dolar_tl_parent.find("span")
            dolar_tl_kur = dolar_tl_span.string
            kur0 = float(dolar_tl_kur)
            sonuc = girdi / kur0

            global l3
            l3 = Label(window, text=sonuc, bg="grey", fg="white")
            l3["font"] = ("Futura", 20)
            l3.pack()

        def clear():
            label0.destroy()
            label1.destroy()
            label2.destroy()
            l3.destroy()

        window.title("Döviz kuru hesaplama")
        window.geometry("400x600")
        window.maxsize(600, 800)
        label = Label(window, text="", bg="grey", fg="beige")
        label.pack()
        label["text"] = ("Döviz Hesaplama")
        label["font"] = ("Arial", 35)
        entry = Entry(window,width=400 ,textvariable=girdi1, bg="dim gray", fg="white")
        entry.pack(pady=5)
        button0 = Button(window, text="$ > ₺", command=press0,bg="dim gray", fg="white",width=400,height=5)
        button1 = Button(window, text="₺ > $", command=press1,bg="dim gray", fg="white",width=400,height=5)
        button2 = Button(window, text="€ > ₺", command=press2,bg="dim gray", fg="white",width=400,height=5)
        button3 = Button(window, text="₺ > €", command=press3,bg="dim gray", fg="white",width=400,height=5)
        button4 = Button(window, text="Temizle",command=clear, bg="dim gray", fg="white", width=400, height=5)
        button0.pack()
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()




window = Tk()
window.iconbitmap("appicon.ico")
window.configure(bg="grey")
arayuz(window)
window.mainloop()