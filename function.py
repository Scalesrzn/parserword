import requests as req
import re
import xlrd, xlwt
import win32api


#Проверка доступности сайта. Если сервер возвращает 200,то сайт доступен
def CheckAccess(url): 
    response = req.get(url)
    if response.status_code == 200:
        access = 'Сайт доступен'
    else:
        access = 'Сайт недоступен ' + str(response)
    return True, print(access)

#Получаем содержимое страницы
def getPage(url,headers):
    html = req.get(url, headers = headers)
    html.encoding = 'UTF-8'
    htmlcode = html.text
    print(htmlcode)
    return htmlcode

def createRequest(word,url,type):
    if type == "Parse":
        requestUrl = 'https://www.bukvarix.com/keywords/?q=' + word
    elif type == "Analys" and url == 'Yandex':
        requestUrl = 'https://www.bukvarix.com/site/?q=' + word + '&region=msk&v=table'
    else:
        requestUrl = 'https://www.bukvarix.com/site/?q=' + word + '&region=gmsk&v=table'
    
    return requestUrl

def createEXCEL(aKeywords,filename):
    wb = xlwt.Workbook()
    style = xlwt.XFStyle()
    style.alignment.wrap = 1
    ws = wb.add_sheet('Keyword')

#    задаем размер колонок и заголовки
    for i in range(0,4):
        ws.col(i).width = 256 * 20

    ws.write(0, 0, 'Ключевое слово')
    ws.write(0, 1, 'Количество слов')
    ws.write(0, 2, 'Количество символов')
    ws.write(0, 3, 'Частотность весь мир')
    ws.write(0, 4, 'Частотность полного вхождения')
#   заполняем строки 
    for i in range(len(aKeywords)):
        try:
            print("Текущее слово", aKeywords[i])
            aKeyString = re.split(r',',str(aKeywords[i]))
            key = aKeyString[0]
            countkey = aKeyString[1]
            countchar = aKeyString[2]
            countworld = aKeyString[3]
            counthardworld =  aKeyString[4]
            #записывает в строки значения
            ws.write(i+1,0,key,style)
            ws.write(i+1,1,countkey,style)
            ws.write(i+1,2,countchar,style)
            ws.write(i+1,3,countworld,style)
            ws.write(i+1,4,counthardworld,style)
        except Exception:
            print('Не удалось сохранить на слове: ' +  aKeywords[i])
    wb.save(filename+".xls")
    win32api.MessageBox(0, 'Успешно сохранено в %s '%(filename), 'Успех!')
