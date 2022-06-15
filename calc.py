import math

list_number = []
f = open( 'calc.txt', 'w' )

def sum():
    sum_list = math.fsum(list_number)
    f.write('сумма введенных чисел равна - '+ str(sum_list))
    f.close()
def mult():
    mult_list = math.prod(list_number)
    f.write('произведение введенных чисел равно - '+ str(mult_list))
    f.close()
    
    
print('если хотите получить сумму введенных чисел наберите SUM')
print('если хотите получить произведение введенных чисел наберите MULT')
print('или вводите цифры')


while True:
    usr = input()
    if usr == 'SUM' or usr == 'sum':
        sum()
        break
    if usr == 'MULT' or usr == 'mult':
        mult()
        break
    list_number.append(int(usr))
    f.write(usr+'\n')
  