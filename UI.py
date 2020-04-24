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
            sParse = Keyword.get()
            sDomain = DomainAnalys.get()
            TextLog.delete(1.0, END)
            TextLog.insert(1.0,"\nВы ввели имя домена: " + sDomain + '\nИ выбрали поисковую систему ' + DropDown.get())
            TextLog.insert(1.0,"Вы ввели ключевую фразу: " + sParse)
            aValue = []
            aValue.append(sParse)
            aValue.append(sDomain)

            return aValue

        #Получаем ответ от сервера в виде HTML документа
        def getValueButton():
            sIntVal = re.split(r",", inputValue()[0])
            for sInputValue in sIntVal: 
                val = function.createRequest(str(sInputValue),DropDown.get(),"Parse")
                print("Сгенерированный HTTP запрос: " + val)
                response = function.getPage(val,headers)
                TextLog.insert(1.0,"Ответ " + response)
                if DropDown.get() == 'Yandex':
                    xPathResponseYandex(response)
                else:
                    xPathResponseGoogle(response)

        #Получаем результаты анализа от сервера
        def getDomainValue():
            sIntVal = re.split(r",", inputValue()[1])
            for sInputValue in sIntVal: 
                val = function.createRequest(str(sInputValue),DropDown.get(),"Analys")
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
            aDirtResponse = []
            aResponse = re.split(r",\[",re.findall(r'\[\".*\d\]', response)[0])
            print(len(aResponse))
            for i in range(len(aResponse)):
                aDirtResponse.append(re.sub(r'[\]\[]','',aResponse[i]))
                aClearResponse.append(re.sub(r'[\]\[]','',aDirtResponse[i])) 
                TextResult.insert(1.0, re.sub(r'[\]\[]','',aClearResponse[i]) + '\n')
                # print(aClearResponse)
            return aClearResponse
        # # Задаем путь для сохранения файла
        # def directory():   
        def saveExcelParse():
            sFilePath = fd.asksaveasfilename(filetypes=( ("Excel files", "*.xls"),
                                                        ("All files", "*.*") ))
            #Проверяем на пустоту путь сохранения файлы и если не пусто, то выполняем сохранение
            if sFilePath != '':
                aClearResponse = []
                aDirtResponse = []
                aAllKeyResponse =[]
                sIntVal = re.split(r",", inputValue()[0])
                for sInputValue in sIntVal: 
                    val = function.createRequest(str(sInputValue),DropDown.get(),"Parse")
                    response = function.getPage(val,headers)
                    aClearResponse = xPathResponseYandex(response)
                    for i in aClearResponse:
                        aAllKeyResponse.append(i)
                function.createEXCEL(aAllKeyResponse,sFilePath)
                # print(aClearResponse)
        
        def saveExcelAnalys():
            sFilePath = fd.asksaveasfilename(filetypes=( ("Excel files", "*.xls"),
                                                        ("All files", "*.*") ))
            #Проверяем на пустоту путь сохранения файлы и если не пусто, то выполняем сохранение
            if sFilePath != '':
                aClearResponse = []
                aDirtResponse = []
                val = function.createRequest(str(inputValue()[1]),DropDown.get(), "Analys")
                #response = function.getPage(val,headers)
                response = TextResult.get(1.0, END)
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
        KeywordLabel = Label(text="Введите ключевое слово или слова через запятую:")
        DropDownLabel = Label(text = 'Выберите поисковую систему:')
        Keyword = Entry()
        DropDown = Combobox(self.parent)
        Close = Button(text="Закрыть", command = closeForm)
        Parse = Button(text = 'Начать парсинг', command = getValueButton)
        TextLog = Text(width=50, height=20)
        TextResult = Text(width=50, height=20)
        SaveValue = Button(text = "Сохранить параметры парсинга", command = inputValue )
        SaveExcel = Button(text = 'Сохранить в EXCEL документ', command = saveExcelParse )
        
        #Интерфейсные объекты для анализа
        DomainAnalysLabel = Label(text="Введите название домена для анализа:")
        DomainAnalys = Entry()
        Analys  = Button(text = 'Начать анализ', command = getDomainValue)
        AnalysSave = Button(text = 'Сохранить в EXCEL документ результаты анализа', command = saveExcelAnalys )
       
        # NameSpace
        DropDown['values'] = ('Yandex', 'Google')  
        DropDown.current(1)  # вариант по-умолчанию

        # Размещаем элементы

        #0-й столбец
        TextLog.grid(row = 0, column = 0)
        KeywordLabel.grid(row = 1, column = 0, sticky="w")
        Keyword.grid(row = 2,column = 0)
        DomainAnalysLabel.grid(row = 3, column = 0, sticky="w")
        DomainAnalys.grid(row = 4,column = 0)
        DropDownLabel.grid(row = 5, column = 0)
        DropDown.grid(row=6, column=0) 
        SaveValue.grid(row = 7, column = 0)

        #1-й столбец
        TextResult.grid(row = 0, column = 1)
        Parse.grid(row = 1, column = 1)
        SaveExcel.grid(row = 2,column = 1)
        Analys.grid(row = 6, column = 1)
        AnalysSave.grid(row = 7, column = 1)
       
        #2-й столбец
        Close.grid(row = 7,column = 3 )

        # Забираем с инпутов значения
        
        # вставка начальных данных
        Keyword.insert(0, "Ключевое слово")
        TextLog.insert(1.0, "Здесь будут отображаться все этапы прохождения программы")