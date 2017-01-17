import re
file  = input("Какой файл открыть (введите путь к файлу)? ")

with open(file, 'r', encoding = 'utf-8') as f:
        i = (len(re.findall(r'\b.+ing\b', f.read())))
        print(i)
        #Сколько в тексте форм на -ing.


#Не разобралась, почему тот же самый код не работает в функции:
import re
file  = input("Какой файл открыть (введите путь к файлу)? ")

def open_file(text):
    with open(file, 'r', encoding = 'utf-8') as f:
        result = len(re.findall(r'\b.+ing\b', f.read()))
        print(result)
