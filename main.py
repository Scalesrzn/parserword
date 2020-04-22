import requests as req
import urllib
import re
import function
import UI
from tkinter import Tk, Frame, BOTH
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}
sWord = 'Привет'
sSiteURL = 'https://www.bukvarix.com/'

def main():
    root = Tk()
    function.CheckAccess(sSiteURL) #Проверка доступности сайта
    function.CheckAccess(sSiteURL)
    UI.Interface(root) #Создаем объект класса Interface
    root.mainloop() #Инициализация UI

if __name__ == '__main__':
    main()