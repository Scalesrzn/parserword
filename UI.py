import tkinter
import sys
from tkinter import *
from tkinter import Tk, Frame, BOTH
from ttk import Frame, Button, Style
# class Table():

class Interface(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()
    
    # Инициализация интерфейса
    def initUI(self):
        
        # Закрытие формы
        def closeForm():  
            sys.exit()  

        # Забираем значение инпута 
        def inputValue():
            value = Keyword.get()
            TextLog.delete(1.0, END)
            TextLog.insert(1.0,"Вы ввели: " + value)
        
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
        # Располагаем объекты на форме
        
        # Объявляем все элементы:
        KeywordLabel = Label(text="Введите имя:")
        Keyword = Entry()
        Close = Button(text="Закрыть", command = closeForm)
        Parse = Button(text = 'Начать парсинг')
        TextLog = Text(width=25, height=5)
        SaveValue = Button(text = "Сохранить параметры парсинга", command = inputValue )
        
        # Размещаем элементы
        KeywordLabel.grid(row = 0, column = 0, sticky="w")
        Keyword.grid(row = 0,column = 1, padx = 5, pady = 5)
        TextLog.grid(row = 2, column = 1)
        SaveValue.grid(row = 2, column = 2)
        Parse.grid(row = 3, column = 2)
        Close.grid(row = 4,column = 2 )
        
        

        # Забираем с инпутов значения
        
        # вставка начальных данных
        Keyword.insert(0, "Ключевое слово")
        TextLog.insert(1.0, "Здесь будут отображаться все этапы прохождения программы")