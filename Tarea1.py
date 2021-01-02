import re

txt = open('prueba.txt')
numeros = list()
suma = 0
for i in txt:
    numeros.extend(re.findall('[0-9]+', i))

for j in numeros:
    suma = suma + int(j)

print(suma)


