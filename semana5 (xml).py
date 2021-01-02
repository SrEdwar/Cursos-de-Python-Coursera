import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
suma = 0
while True:
    address = input('Enter location: ')
    if len(address) < 1: break


    uh = urllib.request.urlopen(address, context=ctx)

    data = uh.read()
    #print('Retrieved', len(data), 'characters')
    #print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('comments/comment')
    #print('Comments count',len(results))
    for items in results:
        print('Name',items.find('name').text)
        print('Count',items.find('count').text)
        numero = int(items.find('count').text)
        suma = suma + numero


print("Suma Total",suma)




