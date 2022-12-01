import sys
import re

def SaveWords (hashmap, lastTitle, wordMap):
    for word in hashmap.keys():
        value = hashmap[word]
        if word in wordMap:
            array = wordMap[word]
            array.append([lastTitle,value])
            wordMap[word] = array
        else:
            wordMap[word] = ([[lastTitle,value]])

wordMap = {}
hashmap = {}
title =""
lastTitle = ""
counter = 0

for line in sys.stdin:
    title, word, count = line.split('\t')

    if title != lastTitle and counter !=0:
        SaveWords(hashmap, lastTitle, wordMap)
        hashmap = {}
    
    lastTitle = title
    counter += 1
    if word in hashmap:
        hashmap[word] += 1
    else:
        hashmap[word] = 1

SaveWords(hashmap, lastTitle, wordMap)

for key, value in wordMap.items():
    print('%s\t%s' % (key,value))