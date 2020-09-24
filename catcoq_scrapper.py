#reruired libraries
import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#open the website

url = "https://catcoq.com/"
html =urlopen(url)

links = soup.find_all('a', href=True)
#for link in links:
#    print (link['href'])

output = ''
blacklist = ['head'
]
whitelist = [
    #'body',
    #'em',
    'h1',
    'h2',
    'h3',
    'p',
    'a'
]

#for t in alltext:
#    if t.parent.name not in blacklist:
#        output += '{} '.format(t)
#output = re.sub("[\n]*", "", output)

for t in alltext:
    if t.parent.name  in whitelist:
        if t.parent.name  not in blacklist:
        output += '{} \n'.format(t)
output = re.sub("[\n]*", "", output)
#output = re.sub("[/  +/g]", "\n", output)

f = open("cleaned_text/catcoq.txt","w+")
f.write(output)
f.close()


{'body',
 'div',
 'em',
 'h1',
 'h2',
 'h3',
 'p',
 '[document]',
 'noscript',
 'header',
 'html',
 'meta',
 'head',
 'input',
 'script',
 'figcaption',
 'button',
 'button',
 'figure',
 'footer',
 'form',
 'svg',
 'label',
 'nav',
 'time',
 'section',
 'span',
 'strong',
 'title'
 'a'
 }
