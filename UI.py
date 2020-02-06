import tkinter
import sys
from tkinter import *
from tkinter import Tk, Frame, BOTH
from ttk import Frame, Button, Style

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()
       
    def initUI(self):
        self.parent.title("Парсер")
        self.style = Style()
        self.style.theme_use("default")
        #Задаем размеры формы
        w = 600
        h = 500
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y)) 
        #Располагаем объекты на форме
        Keyword = Label(text="Введите имя:")
        Keyword.grid(row=0, column=0, sticky="w")
        Keyword = Entry()
        Keyword.grid(row=0,column=1, padx=5, pady=5)
        # вставка начальных данных
        Keyword.insert(0, "Ключевое слово")
    def CloseForm(self):  
        sys.exit()