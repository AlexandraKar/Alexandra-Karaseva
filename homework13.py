#Программа должна просмотреть все папки и файлы, находящиеся в одной папке с ней, и сообщить следующую информацию
#1. Сколько найдено папок, содержащих цифры в названии.

import os
import re

l = 0
folder = []

p = re.compile(r"[0-9]+", re.U)

for root, dirs, files in os.walk('.'):
    for d in dirs:
        if p.search(d):
            folder.append(d)
            l += 1

print('Всего найдено {} папок с цифрами в названии.'.format(l))
print('\nВот они:')
for x in folder:
    print(x)
