import requests as req
#Word - слова для поиска
#SiteURL - Адрес сайта
#Headers - заголовок запроса
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/39.0.2171.95 Safari/537.36'}
Word = 'Привет'
SiteURL = 'https://www.bukvarix.com/'


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



# def SearchWord(Word):
#     hello=hello