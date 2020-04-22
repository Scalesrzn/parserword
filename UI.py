import tkinter
import main
import sys
from lxml import etree 
import lxml.html as ht
from tkinter import *
from tkinter import Tk, Frame, BOTH
from tkinter import filedialog as fd
from ttk import Frame, Button, Style, Combobox
import function
# class Table():

class Interface(Frame):
   
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()
    
    # Инициализация интерфейса
    def initUI(self):

        # master = Frame(self)
        #Headers - заголовок запроса
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/39.0.2171.95 Safari/537.36'}
        aClearResponse = []
        # Закрытие формы
        def closeForm():  
            sys.exit()  

        # Забираем значение инпута 
        def inputValue():
            value = Keyword.get()
            TextLog.delete(1.0, END)
            TextLog.insert(1.0,"Вы ввели: " + value + '\nИ выбрали поисковую систему ' + DropDown.get())
            return value

        #Получаем ответ от сервера в виде HTML документа
        def getValueButton():
            val = function.createRequest(str(inputValue()),DropDown.get())
            print("Сгенерированный HTTP запрос: " + val)
            response = function.getPage(val,headers)
            TextLog.insert(1.0,"Ответ " + response)
            if DropDown.get() == 'Yandex':
                xPathResponseYandex(response)
            else:
                xPathResponseGoogle(response)

        def xPathResponseGoogle(response):
            print('Арбайтен')

        def xPathResponseYandex(response):
            #Разделяем полученную строку на список и убираем []
            aClearResponse = []
            aResponse = re.split(r",\[",re.findall(r'\[\".*\d\]', response)[0])
            print(len(aResponse))
            for i in range(len(aResponse)):
                aClearResponse.append(re.sub(r'[\]\[]','',aResponse[i])) 
                TextResult.insert(1.0, re.sub(r'[\]\[]','',aClearResponse[i]) + '\n')
                print(aClearResponse)
        
        # # Задаем путь для сохранения файла
        # def directory():   
  
        def saveExcel():
            sFilePath = fd.asksaveasfilename(filetypes=( ("Excel files", "*.xls"),
                                                        ("All files", "*.*") ))
            #Проверяем на пустоту путь сохранения файлы и если не пусто, то выполняем сохранение
            if sFilePath != '':
                aClearResponse = []
                aDirtResponse = []
                val = function.createRequest(str(inputValue()),DropDown.get())
                response = function.getPage(val,headers)
                aResponse = re.split(r",\[",re.findall(r'\[\".*\d\]', response)[0])
                for i in range(len(aResponse)):
                    aDirtResponse.append(re.sub(r'[\]\[]','',aResponse[i]))
                    aClearResponse.append(re.sub(r'[\]\[]','',aDirtResponse[i]))
                # вызов функции создания EXCEL
                function.createEXCEL(aClearResponse,sFilePath)
                print(aClearResponse)

        #Получаем значение из выпадающег осписка
        # value = (listbox.get(listbox.curselection()))


        self.parent.title("Парсер")
        self.style = Style()
        self.style.theme_use("default")

        #Задаем размеры формы
        w = 1200
        h = 500
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y)) 
        


 

        # Располагаем объекты на форме
        # Объявляем все элементы:
        KeywordLabel = Label(text="Введите ключевое слово:")
        DropDownLabel = Label(text = 'Выберите поисковую систему:')
        Keyword = Entry()
        DropDown = Combobox(self.parent)
        Close = Button(text="Закрыть", command = closeForm)
        Parse = Button(text = 'Начать парсинг', command = getValueButton)
        TextLog = Text(width=50, height=20)
        TextResult = Text(width=50, height=20)
        SaveValue = Button(text = "Сохранить параметры парсинга", command = inputValue )
        SaveExcel = Button(text = 'Сохранить в EXCEL документ', command = saveExcel )
       
        # NameSpace
        DropDown['values'] = ('Yandex', 'Google')  
        DropDown.current(1)  # вариант по-умолчанию

        # Размещаем элементы
        KeywordLabel.grid(row = 0, column = 2, sticky="w")
        Keyword.grid(row = 0,column = 3)
        DropDownLabel.grid(row = 1, column = 0)
        # self.DropDown.grid(row = 1, column = 1)
        SaveValue.grid(row = 3, column = 1)
        SaveExcel.grid(row = 5,column = 1)
        Parse.grid(row = 4, column = 1)
        TextLog.grid(row = 0, column = 0)
        TextResult.grid(row = 0, column = 1)
        DropDown.grid(column=0, row=3) 
        Close.grid(row = 5,column = 3 )



        
        

        # Забираем с инпутов значения
        
        # вставка начальных данных
        Keyword.insert(0, "Ключевое слово")
        TextLog.insert(1.0, "Здесь будут отображаться все этапы прохождения программы")