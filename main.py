import requests as req
import urllib
import re
import function
import UI
from tkinter import Tk, Frame, BOTH
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/39.0.2171.95 Safari/537.36'}
Word = 'Привет'
SiteURL = 'https://www.bukvarix.com/'

def main():
    root = Tk()
    ex = UI.Example(root)
    root.mainloop() 
function.CheckAccess(SiteURL)

if __name__ == '__main__':
    main()