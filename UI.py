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
import win32api
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
                xPathResponse(response,sInputValue)

        #Получаем результаты анализа от сервера
        def getDomainValue():
            sIntVal = re.split(r",", inputValue()[1])
            for sInputValue in sIntVal: 
                val = function.createRequest(str(sInputValue),DropDown.get(),"Analys")
                print("Сгенерированный HTTP запрос: " + val)
                response = function.getPage(val,headers)
                TextLog.insert(1.0,"Ответ " + response)
                xPathResponse(response,sInputValue)

        def xPathResponse(response,keyword):
            #Разделяем полученную строку на список и убираем []
            aClearResponse = []
            aDirtResponse = []
            try:
                aResponse = re.split(r",\[",re.findall(r'\[\".*\d\]', response)[0])
                print(len(aResponse))
                for i in range(len(aResponse)):
                    aDirtResponse.append(re.sub(r'[\]\[]','',aResponse[i]))
                    aClearResponse.append(re.sub(r'[\]\[]','',aDirtResponse[i])) 
                    TextResult.insert(1.0, re.sub(r'[\]\[]','',aClearResponse[i]) + '\n')
                    # print(aClearResponse)
            except Exception:
                 win32api.MessageBox(0, 'Запрос "%s" ничего не вернул :('%(keyword), 'Ошибка!')
                 aClearResponse = 'Error'
            return aClearResponse
        # # Задаем путь для сохранения файла
        # def directory():   
        def saveExcel(type):
            sFilePath = fd.asksaveasfilename(filetypes=( ("Excel files", "*.xls"),
                                                        ("All files", "*.*") ))
            #Проверяем на пустоту путь сохранения файлы и если не пусто, то выполняем сохранение
            if sFilePath != '':
                aClearResponse = []
                aAllKeyResponse = []
                sError = []
                #Проверка, откуда произошел вызов функции
                if type == "Parse":
                    sIntVal = re.split(r",", inputValue()[0])
                else:
                    sIntVal = re.split(r",", inputValue()[1])

                for sInputValue in sIntVal: 
                    val = function.createRequest(str(sInputValue),DropDown.get(),type)
                    response = function.getPage(val,headers)
                    aClearResponse = xPathResponse(response,sInputValue)
                    if aClearResponse == 'Error':
                        sError.append(sInputValue + " Error")
                    else:
                        for i in aClearResponse:
                            aAllKeyResponse.append(i)
                
                ##Проверка на ошибки
                if len(sError) == len(sIntVal):
                    win32api.MessageBox(0, 'Ни один из запросов не дал результатов. Файл не будет сохранен', 'Ошибка!')
                elif len(sError) > 1:   
                    win32api.MessageBox(0, 'Не удалось сохранить все, что было указано в запросе! Скорее всего один из запросов не дал результатов', 'Ошибка!')
                    function.createEXCEL(aAllKeyResponse,sFilePath)
                else:
                    function.createEXCEL(aAllKeyResponse,sFilePath)
        
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
        SaveExcel = Button(text = 'Сохранить в EXCEL документ', command = lambda: saveExcel ('Parse') )
        
        #Интерфейсные объекты для анализа
        DomainAnalysLabel = Label(text="Введите название домена для анализа:")
        DomainAnalys = Entry()
        Analys  = Button(text = 'Начать анализ', command = getDomainValue)
        AnalysSave = Button(text = 'Сохранить в EXCEL документ результаты анализа', command = lambda: saveExcel ('Analys') )
       
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