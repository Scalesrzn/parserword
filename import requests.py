import requests
import time
import re
from bs4 import BeautifulSoup
user_id = 'Hello'

s = requests.Session() 
s.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    })

def load_user_data(session):
    url = 'https://keywordtool.io/ru/search/keywords/google/391766?category=web&keyword=' + 'hello' +'&__cf_chl_jschl_tk__=8196155626232b5e9a316286d75e6095283ed33d-1585443715-0-AY9LgEg98tmjZsaAy8fWQmatPEvIEFbJGZ-na0T1ERW31Ln2YJF7v2RwCN6_PU5062iH2nYKjtSWssY8Tk0ddj7LZyvpXlqN6p8ZtaQXYbK11nuBJilk-TTcQq6_ZTI5HopkFXXk4BtxGMinFacORExsel1ga_Fp0I7tZ9x-Xww0ELpO5Tmpm0s5t6ocmaQeDxAZeXuocMyqxVurqrXuJhL0LcXfGMMJAlb9rcTsAq19v99AOB7DQtHEcSR8IRFROcUQTXLzlP-4vHdP6A8MfUs3JnP5lsMQRC-EzGU48_VI48pS1Y2TnWYGk3MOvaq6FRgJ1TpgJb-pw0XaugwM31ZCcwKPoWBj3QC6wijVD7c6H_LT2WZAFIBK24CDlWll8JI6F0PqGL5WxlBgt8bSRmUBclKEPsXNxgEOIxXvBnWv#suggestions'
    request = session.get(url)
    request.encoding = 'UTF-8'
    # хочу получить action из
    requests = 
    time.sleep(5)
    request = session.get(url)
    request.encoding = 'UTF-8'
    htmlcode = request.text
    print (htmlcode)
    return request.text

def contain_movies_data(text):
    soup = BeautifulSoup(text)
    return soup

load_user_data(s)
