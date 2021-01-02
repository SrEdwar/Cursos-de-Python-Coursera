"""
import ssl
from urllib.request import urlopen

from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

suma = 0
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')

for tag in tags:
    print('TAG:', tag)
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
    suma = suma + int(tag.contents[0])

print(suma)
"""


# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

nombreFinal = None
contador = 0
url = input('Enter - ')
count = int(input("Count - "))
position = int(input('Position - '))
position = position-1
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')

while contador < count:
    url= tags[position].get('href', None)
    print(url)
    separar=url.split("_")
    separar = separar[2].split(".")
    separar = separar[0]
    nombreFinal = separar
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    contador+=1



print("Nombre final: ",nombreFinal)