#coding utf-8
import random

def noun(syllables):
    file = open('nouns_' + syllables + '.txt','r', encoding = 'utf-8')
    text = file.read()
    verbs = text.split('\n')
    return random.choice(verbs)

def verb(syllables):
    file = open('verbs_' + syllables + '.txt','r', encoding = 'utf-8-')
    text = file.read()
    verbs = text.split('\n')
    return random.choice(verbs)

def punctuation():
    marks = ['.', ',', '?', '!', '', '-', '...', '?!']
    return random.choice(marks)

def stroka_5():
    return noun('2') + ' ' + verb('3') + punctuation()

def stroka_7():
    return noun('4') + ' ' + verb('3') + punctuation()

def create_poem():
    return stroka_5() + '\n' + stroka_7() + '\n' + stroka_5()

print(create_poem())
