import random

mss1 = ["_","_","_"]
mss2 = ["_","_","_"]
mss3 = ["_","_","_"]

def printP():
  print("    1    2    3")
  print("A",mss1)
  print("B",mss2)
  print("C",mss3)

printP()

def win():
    #1 
    if mss1[0] == mss1[1] == mss1[2]:
        if mss1[0] == 'X':
            print('ПОБЕДА ПОЛЬЗОВАТЕЛЯ')
            exit("игра завершена")
        if mss1[0] == '0':
            print('ПОБЕДА БОТА')
            exit("игра завершена")
    #2
    if mss2[0] == mss2[1] == mss2[2]:
        if mss2[0] == 'X':
            print('ПОБЕДА ПОЛЬЗОВАТЕЛЯ')
            exit("игра завершена")
        if mss2[0] == '0':
            print('ПОБЕДА БОТА')
            exit("игра завершена")
    #3
    if mss3[0] == mss3[1] == mss3[2]:
        if mss3[0] == 'X':
            print('ПОБЕДА ПОЛЬЗОВАТЕЛЯ')
            exit("игра завершена")
        if mss3[0] == '0':
            print('ПОБЕДА БОТА')
            exit("игра завершена")  
    #4
    if mss1[0] == mss2[0] == mss3[0]:
        if mss1[0] == 'X':
            print('ПОБЕДА ПОЛЬЗОВАТЕЛЯ')
            exit("игра завершена")
        if mss1[0] == '0':
            print('ПОБЕДА БОТА')
            exit("игра завершена") 
    #5
    if mss1[1] == mss2[1] == mss3[1]:
        if mss1[1] == 'X':
            print('ПОБЕДА ПОЛЬЗОВАТЕЛЯ')
            exit("игра завершена")
        if mss1[1] == '0':
            print('ПОБЕДА БОТА')
            exit("игра завершена") 
    #6
    if mss1[2] == mss2[2] == mss3[2]:
        if mss1[2] == 'X':
            print('ПОБЕДА ПОЛЬЗОВАТЕЛЯ')
            exit("игра завершена")
        if mss1[2] == '0':
            print('ПОБЕДА БОТА')
            exit("игра завершена") 
    #7
    if mss1[0] == mss2[1] == mss3[2]:
        if mss1[0] == 'X':
            print('ПОБЕДА ПОЛЬЗОВАТЕЛЯ')
            exit("игра завершена")
        if mss1[0] == '0':
            print('ПОБЕДА БОТА')
            exit("игра завершена") 
    #8
    if mss1[2] == mss2[1] == mss3[0]:
        if mss1[2] == 'X':
            print('ПОБЕДА ПОЛЬЗОВАТЕЛЯ')
            exit("игра завершена")
        if mss1[2] == '0':
            print('ПОБЕДА БОТА')
            exit("игра завершена")      


             
def Bot():
    r = random.randint(1,3)
    if r == 1:
        r = random.randint(0,2)
        if mss1[r] == "_":
            mss1[r]="0"
        else:
            Bot()
    elif r == 2:
        r = random.randint(0,2)
        if mss2[r] == "_":
            mss2[r]="0"
        else:
            Bot()
    elif r == 3:
        r = random.randint(0,2)
        if mss3[r] == "_":
            mss3[r]="0"
        else:
            Bot()


i=1       
while   i<=4:
  user = input("-> ")
  if user == "A1" or user == "a1":
    if mss1[0] == "_":
      mss1[0] = "X"
      Bot()
    else:
      print("No ")
  elif user == "A2" or user == "a2":
    if mss1[1] == "_":
      mss1[1] = "X"
      Bot()
    else:
      print("No ")
  elif user == "A3" or user == "a3":
    if mss1[2] == "_":
      mss1[2] = "X"
      Bot()
    else:
      print("No ")
  elif user == "B1" or user == "b1":
    if mss2[0] == "_":
      mss2[0] = "X"
      Bot()
    else:
      print("No ")
  elif user == "B2" or user == "b2":
    if mss2[1] == "_":
      mss2[1] = "X"
      Bot()
    else:
      print("No ")
  elif user == "B3" or user == "b3":
    if mss2[2] == "_":
      mss2[2] = "X"
      Bot()
    else:
      print("No ")
  elif user == "C1" or user == "c1":
    if mss3[0] == "_":
      mss3[0] = "X"
      Bot()
    else:
      print("No ")
  elif user == "C2" or user == "c2":
    if mss3[1] == "_":
      mss3[1] = "X"
      Bot()
    else:
      print("No ")
  elif user == "C3" or user == "c3":
    if mss3[2] == "_":
      mss3[2] = "X"
      Bot()
    else:
      print("No ")

  printP()
  
  win()
  i=i+1
else:
    exit('НИЧЬЯ')