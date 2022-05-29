
import random
import string
text=[]
fraz = 100 #генератор 100 фраз
letters = string.ascii_lowercase


i=1
while i <= fraz:
    word_col=random.randint(1, 10)#количество слов в фразе
    x=1
    while x<=word_col:
        y=1
        word_lenght = random.randint(1, 12) #длинна слова до 12 букв
        word=''.join(random.choice(letters)for i in range(word_lenght))
        #print(word)
        text.append(word)
        file = open('text_generator.txt', 'a')
        file.write(word+' ')
        file.close()
        x=x+1
    file = open('text_generator.txt', 'a')
    file.write('\n')
    file.close()
    print(text)
    i=i+1


