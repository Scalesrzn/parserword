import tkinter
import main
import sys
from lxml import etree 
import lxml.html as ht
from tkinter import *
from tkinter import Tk, Frame, BOTH
from ttk import Frame, Button, Style
import function
# class Table():

class Interface(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()
    
    # Инициализация интерфейса
    def initUI(self):
        #Headers - заголовок запроса
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/39.0.2171.95 Safari/537.36'}
        
        # Закрытие формы
        def closeForm():  
            sys.exit()  

        # Забираем значение инпута 
        def inputValue():
            value = Keyword.get()
            TextLog.delete(1.0, END)
            TextLog.insert(1.0,"Вы ввели: " + value)
            return value
        
        #Получаем ответ от сервера в виде HTML документа
        def getValueButton():
            val = function.createRequest(str(inputValue()),main.sSiteURL)
            print("Сгенерированный HTTP запрос: " + val)
            response = function.getPage(val,headers)
            TextLog.insert(1.0,"Ответ " + response)
            xPathResponse(response)

        def xPathResponse(response):
            
            # DOM = etree.parse(response)
            # sString = DOM.xpath('/tr/td')
            # print("LOL" + sString)
            # for l in sString:
            #     TextResult.insert(1.0, l.get( 'href' )) 
            TextResult.insert(1.0, re.findall("\"data\"*\]\]", response))
            print(re.findall('\"data\"*\[*\]*', response))
  
        
            

        self.parent.title("Парсер")
        self.style = Style()
        self.style.theme_use("default")

        #Задаем размеры формы
        w = 500
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
        Parse = Button(text = 'Начать парсинг', command = getValueButton)
        TextLog = Text(width=50, height=20)
        TextResult = Text(width=50, height=20)
        SaveValue = Button(text = "Сохранить параметры парсинга", command = inputValue )
        # Размещаем элементы
        KeywordLabel.grid(row = 0, column = 0, sticky="w")
        Keyword.grid(row = 0,column = 1, padx = 5, pady = 5)
        SaveValue.grid(row = 0, column = 3)
        TextLog.grid(row = 1, column = 1)
        TextResult.grid(row = 1, column = 2)
        Parse.grid(row = 1, column = 3)
        Close.grid(row = 2,column = 3 )
        
        

        # Забираем с инпутов значения
        
        # вставка начальных данных
        Keyword.insert(0, "Ключевое слово")
        TextLog.insert(1.0, "Здесь будут отображаться все этапы прохождения программы")