#!/usr/bin/env python
# -*-coding:utf-8 -*

import sys
import re

title = sys.stdin.readline().split(":")[1].strip()

for line in sys.stdin:
    line = line.strip()

    if line.startswith("Title:"):
        title = line.split(":")[1].strip()
    
    words = re.split('\W+', line)

    words = [word for word in words if not word.isdigit() and len(word) > 1]
    words = [word.lower() for word in words]

    for word in words:

        if word!= '':
            print('%s\t%s\t%s' % (title, word, 1))