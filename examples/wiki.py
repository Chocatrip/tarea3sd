#!/usr/bin/env python
# -*-coding:utf-8 -*

import wikipedia as wiki
import regex as re
wiki.set_lang("es")

pages = []
pages.append('Inquisicion')
pages.append('Guerra santa')
pages.append('Brujeria')
pages.append('Herejia en el catolicismo')
pages.append('Color')
pages.append('Idioma griego')
pages.append('Caballeros Templarios')
pages.append('Orden militar')
pages.append('Orden de malta')
pages.append('Palacio magistral de la orden de malta')

counter = 0

for page in pages:
    a = wiki.page(page)
    
    page = page.strip().replace(" ", "_")
    array = a.content.split(" ")
    path = "./"

    if counter < 5:
        path = path + "docs1/" + page + ".txt"
    else:
        path = path + "docs2/" + page + ".txt"
    
    f = open(path, "w")
    f.write("Title: " + page + "\n")

    for i in array:
        f.write(i + " ")
    counter += 1
