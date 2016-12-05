#3 вариант
file = open('text.txt','r',encoding='utf-8')
length1 = 0
length3 = 0
for word in file:
    if len(word) == 1:
        length1 += 1
    elif len(word) == 3:
        lenght3 += 1
        
if length1 == 0:
    print('No words with length of 1 symbol')
elif length3 == 0:
    print('No words with length of 3 symbols')
else:
    print('In file '+str(length3/length1)+' times more words of length 3 than of words of length 1')
file.close()

#Не вижу ошибки, не понимаю, почему программа не видит слова из одного символа.
