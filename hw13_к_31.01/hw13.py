#В этом домашнем задании программа должна открывать файл с русским текстом в кодировке UTF-8 и распечатывать из него по одному разу все встретившиеся в нём (в зависимости от варианта):
#1. формы глагола "открыть"
#В формы глагола включаются деепричастия, причастия и формы на -ся и не включаются видовые пары (тем более что не у всех из перечисленных глаголов они имеются).

import re

with open ('text.txt', 'r', encoding = 'utf-8') as f:
    text = f.read()
    result = re.finditer('откр(ы((т(ый|ь))|л(а|о|и)?|в(ший?)?)|о(й(те|ся)?|ют?|е(шь|те?|м)))', text)
    for match in result:
        print(match.group())
