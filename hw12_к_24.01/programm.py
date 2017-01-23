#Программа должна уметь загадывать как минимум 5 разных слов (с разными подсказками).
#1 вариант. Пользователю даётся столько попыток угадать слово, сколько букв в слове;

import csv

def lets_play():
    words = {}
    with open('words.csv', 'r', encoding='utf-8') as f:
        text = csv.reader(f, delimiter=',')
        for row in text:
            words[row[0]] = row[1]
    n = 0
    keys = list(words.keys())
    while n < len(words):
        i = 0
        while i <= len(words):
            if i < len(words):
                resp = input(keys[n] + ' ')
                if resp == words[keys[n]]:
                    print('You rock!')
                    n+=1
                    break
                else:
                    print('No. You have ' +str(len(words[keys[n]]))+' more guesses.')
                    i+=1
            else:
                print('Sorry, but you have run out of guesses. The right answer is '+keys[n]+' '+words[keys[n]])
                n+=1

c = lets_play()
