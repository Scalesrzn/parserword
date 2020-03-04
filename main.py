import requests as req
import urllib
import re
import function
import UI
from tkinter import Tk, Frame, BOTH
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/39.0.2171.95 Safari/537.36'}
sWord = 'Привет'
sSiteURL = 'https://www.bukvarix.com/'

def main():
    root = Tk()
    function.CheckAccess(sSiteURL)
    UI.Interface(root) #Создаем объект класса Interface
    root.mainloop() 

if __name__ == '__main__':
    main()