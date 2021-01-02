import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

suma = 0
while True:
    address = input('Enter location: ')
    if len(address) < 1: break


    url = urllib.request.urlopen(address, context=ctx)

    data = url.read()

    info = json.loads(data)


    for i in info['comments']:
        suma = suma+int(i['count'])
    print(suma)




