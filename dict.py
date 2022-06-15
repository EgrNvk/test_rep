import random

mssEn = ['apple','orange','lemon','tomato','cherry','banana','melon','peach','plum']
mssUa = ['яблоко','апельсин','лимон','помидор','вишня','банан','дыня','персик','слива']

def n():
    yes=0
    no=0
    while True:
        r = random.randint(0,len(mssUa)-1)
        print(mssEn[r])
        usr = input('введите перевод ')
        if usr == 'stop' or usr =='STOP':
            print('правильных ответов - ', yes)
            print('неправильных ответов - ', no)
            exit('программа завершена')
        if usr == mssUa[r]:
            print('ВЕРНО')
            yes=yes+1
        else:
            print('НЕ ВЕРНО, ПРАВИЛЬНЫЙ ОТВЕТ - ',mssUa[r])
            no=no+1
            
            
def h():
    yes=0
    no=0
    while True:
        r = random.randint(0,len(mssUa)-1)
        print(mssEn[r])
        answer = [mssUa[r],random.choice(mssUa),random.choice(mssUa),random.choice(mssUa)]
        print('\n', '1 - ', answer[0], '\n', '2 - ', answer[1], '\n', '3 - ',answer[2], '\n', '4 - ', answer[3], '\n')
        usr = input('выберите правильный вариант ')
        if usr == 'stop' or usr =='STOP':
            print('правильных ответов - ', yes)
            print('неправильных ответов - ', no)
            exit('программа завершена')
        if usr == str(1):
            print('ВЕРНО')
            yes=yes+1
        else:
            print('НЕ ВЕРНО, ПРАВИЛЬНЫЙ ОТВЕТ - ',mssUa[r])
            no=no+1
        
        
print('для окончания занятия наберите STOP')
usr = input('перевод с подсказками? нажмите H, без подсказок нажмите N ')
if usr == 'n' or usr == 'N':
    n()
if usr == 'h' or usr == 'H':
    h()
