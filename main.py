import requests as req
import re
#Word - слова для поиска
#SiteURL - Адрес сайта

Word = 'Привет'
SiteURL = 'https://www.bukvarix.com/'
#Проверка доступности сайта. Если сервер возвращает 200,то сайт доступен
def CheckAccess(SiteURL): 
    response = req.get(SiteURL)
    if response.status_code == 200:
        access = 'Сайт доступен'
    else:
        access = 'Сайт недоступен' + response
    return True, print(access)


def SearchWord(Word):
    hello = 'hello'


Check = CheckAccess(SiteURL)[0]
print(Check)