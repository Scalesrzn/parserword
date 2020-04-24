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
        if url == 'Yandex':
            requestUrl = 'https://www.bukvarix.com/keywords/?q=' + word
        else:
            requestUrl = 'https://keywordtool.io/ru/search/keywords/google/391766?category=web&keyword=' + word +'/ru/search/keywords/google/391766?category=web&amp;keyword=%D0%9A%D0%BB%D1%8E%D1%87%D0%B5%D0%B2%D0%BE%D0%B5%20%D1%81%D0%BB%D0%BE%D0%B2%D0%BE&amp;__cf_chl_jschl_tk__=76f1c5c2a038afc8dbe6d12d91bf16c88e03f744-1585445735-0-ARQj6MSDaZqGT-weUgW0VA0VUjp2AfFiV8CYa63-emLJMyyfhK6Ten6QTtwqh3V22HpaNKe6HMZ-6oyjFfurJ8meCE41WpeuTz79hnCruoYbsTXfd8HoLtBSa7YGJWwQDkEGur2foPd1LItRgsq7RsrYI9lKn6QIoJPllkY0tURO5jW7vLg2DpTPh4XbDzmrMkMSC2zwSzHOPSkfOlfd1-1s5b8Qnb4Pyx04ZwAchfYEtnpIId-CWLvLeY0enHMmrzTi_M2VvH1PhwKM2_bcQ5Bxx4I3eUc9DdMCwpgQLwTZcjWquPEf1l1zVHKps1DwT3M7ZSSz0NK6cVv1A3L2mleVxTi1NXNT2ot_1uNc_SMrN8wC7rXWuitmsDNAg_eZ1ldw6_iRsTKd-bcF5TV5kNmG_dIvxB3d3c2S5hEB7CYEluJWCN4WEbFZKvfgSMv8C96fFZS2ACFpZadpSDoUguZ7tIF0ghXi-xLQjwa066nZZztiSUZMAxEQnuxrWCaryg" method="POST" enctype="application/x-www-form-urlencoded"'
    if type == "Analys":
        if url == 'Yandex':
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
    wb.save(filename+".xls")
    win32api.MessageBox(0, 'Успешно сохранено в %s '%(filename), 'Успех!')
