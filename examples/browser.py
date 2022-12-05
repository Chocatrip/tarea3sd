#!/usr/bin/env python
# -*-coding:utf-8 -*

import wikipedia as wiki
import regex as re
import sys
from unidecode import unidecode
wiki.set_lang("es")

def get_url(title):
    return wiki.page(title).url

f = open('data.txt', 'r')
lines = f.readlines()

print('Ingrese palabras a buscar separadas por espacio')

# #read line from sys stdin and split by space
words = sys.stdin.readline().split(' ')
# #remove \n from last word
words[-1] = words[-1].strip()


for line in lines:
    line = line.strip()
    # split by tab
    line = line.split('\t')
    palabra = line[0]
    #palabra to unidecode   
    palabra = unidecode(palabra)
    #if palabra in words:
    if palabra in words:
        data = line[1]
        # data remove first and last character
        data = data[1:-1]
        # split by comma ignoring commas inside brackets
        data = re.split(r',\s*(?![^()]*\))', data)
        #remove special characters from every string on data
        data = [re.sub(r'[^\w\s]','',i) for i in data]
        counter = 0
        
        titles = []
        q = []
        for i in data:
            if counter % 2 == 0:
                titles.append(i)
            else:
                q.append(i)
            counter += 1
        
        print('Palabra: ' + palabra)
        for i in range(len(titles)):
            url = get_url(titles[i])
            toPrint = '|Titulo: ' + titles[i] + '| Cantidad: ' + q[i] + '| URL: ' + url + '|\n'
            for i in range(len(toPrint)):
                print('-', end ='')
            print('\n', end = '')
            print(toPrint, end='')
            for i in range(len(toPrint)):
                print('-', end ='')
            print('\n')
    




