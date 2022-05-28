class Users:
    def __init__(self, login, password):
        self.login = login
        self.password = password
def full_list():#секретный список
    u = open("users.txt", "r")
    p = open("userspass.txt", "r")
    while True:
        user = u.readline()
        password = p.readline()
        if not user:
            break
        print('ПОЛЬЗОВАТЕЛЬ:',user,'ПАРОЛЬ:',password)
        u.close
        p.close
        
usr_choise = input('просмотреть пользователей [L] или добавить нового [N]? ')
if usr_choise == "S" or usr_choise == "s":
    full_list()
if usr_choise == "L" or usr_choise == "l":
    f = open("users.txt", "r")
    print(f.read())
    f.close()
if usr_choise == "N" or usr_choise == "n":
    new_login = input('Введите имя нового пользователя - ')
    new_pass =input('Введите пароль нового пользователя - ')
    new_user = Users(new_login,new_pass)
    f = open("users.txt", "r")
    text=f.read()
    if new_login in text:
        print('такой пользователь существует')
        f.close()
        exit("программа завершена")
    else:
       f = open("users.txt", "a")
       f.write(new_login+'\n')
       f.close()
       f = open('userspass.txt','a')
       f.write(new_pass+'\n')
       f.close
       #print(new_user.login,new_user.password)
