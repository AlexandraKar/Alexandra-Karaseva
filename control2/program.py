import re

with open('text.txt', 'r', encoding='utf-8') as f:
    exclude = '</teiHeader>'
    f.readline()
    i = 0
    for line in f:
        if exclude in line:
            break
        else:
            i+=1
    with open('numbers_of_lines.txt', 'w', encoding = 'utf-8') as m:
        m.write(str(i))   
        
