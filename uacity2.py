import random

with open("ua.txt", "r",encoding="utf-8") as f:
    mss = []
    for line in f:
        mss.append(line.rstrip('\n'))
mss_move = []

def hint():
    x=0
    first_sym = last_sym   
    for i in mss:
        if (i[0] == first_sym) and (i not in mss_move):
            print('подсказка - ',i)
            x=1
            break
    if x==0:
        exit('на букву - '+last_sym+' городов больше нет')
                
    
def usr_move():
    first_sym = usr[0]
    '''if usr == 'hint' or usr =='HINT':
        hint() '''
    if first_sym == last_sym:
        if usr not in mss_move:
            if usr in mss:
                mss_move.append(usr)
                comp_move()
            else:
                print('такого города не существует')
        else:
            print('такой город уже был, введите другой')
    else:
        print('назовите город на - '+last_sym+'\n')

def comp_move():
    print("+++++++++++++")
    last_city = mss_move[-1]
    last_sym = last_city[-1]
    if last_sym == 'ь' or last_sym == 'ъ' or last_sym == 'ы' or last_sym == 'й':
        last_sym = last_city[-2]
    first_sym = last_sym   
    x=0
    for i in mss:
        if (i[0] == first_sym) and (i not in mss_move):
            print('комьютер называет - ',i)
            mss_move.append(i)
            x=1
            break
    if x==0:
        exit('Компьютер проиграл, городов на '+first_sym+' больше нет')
    
print('+++++++++++++++++++++++++++')
print('для окончания наберите STOP')
print('для подсказки наберите HINT')
print('+++++++++++++++++++++++++++')


move=random.choice(mss)
print(move)
mss_move.append(move)

while True:
    last_city = mss_move[-1]
    last_sym = last_city[-1]
    if last_sym == 'ь' or last_sym == 'ъ' or last_sym == 'ы' or last_sym == 'й' or last_sym == 'ц':
        last_sym = last_city[-2]
    usr = input('назовите город на - '+last_sym+'\n')
    if usr == 'stop' or usr =='STOP':
        exit('игра завершена')
    if usr == 'hint' or usr =='HINT':
        hint()    
    usr_move()
    
