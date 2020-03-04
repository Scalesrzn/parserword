import requests as req
#Word - слова для поиска
#SiteURL - Адрес сайта

sWord = 'Привет'
sSiteURL = 'https://www.bukvarix.com/'


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
    return htmlcode

def createRequest(word,url):
    requestUrl = 'https://www.bukvarix.com/keywords/?q=' + word
    return requestUrl

# def SearchWord(Word):
#     hello = hello