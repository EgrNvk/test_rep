

# импортируем модуль для работы со случайными числами
import random
import logging

logging.basicConfig(filename="numbers.log",filemode="w",level=logging.DEBUG)
logging.debug('=======================================')
# число попыток угадать
guesses_made = 0

# получаем имя пользователя из консольного ввода
name = input('Привет! Как тебя зовут?\n')
logging.debug('пользователь ввел имя - '+name)

# получаем случайное число в диапазоне от 1 до 30
number = random.randint(1, 30)
print ('Отлично, {0}, я загадал число между 1 и 30. Сможешь угадать?'.format(name))

# пока пользователь не превысил число разрешенных попыток - 6
while guesses_made < 6:
    
    # получаем число от пользователя
    guess = int(input('Введи число: '))
    logging.debug('пользователь ввел число') 
    logging.debug(guess)
    # увеличиваем счетчик числа попыток
    guesses_made += 1

    if guess < number:
        print ('Твое число меньше того, что я загадал.')

    if guess > number:
        print ('Твое число больше загаданного мной.')

    if guess == number:
        break

if guess == number:
    print ('Ух ты, {0}! Ты угадал мое число, использовав {1} попыток!'.format(name, guesses_made))
    logging.debug('пользователь ')
    logging.debug(name)
    logging.debug('угадал загаданное число')
    logging.debug(number)
    logging.debug('использовав')
    logging.debug(guesses_made)
    logging.debug('попыток')
else:
    print ('А вот и не угадал! Я загадал число {0}'.format(number))
    logging.debug('пользователь ')
    logging.debug(name)
    logging.debug('не угадал загаданное число')
    logging.debug(number)
    logging.debug('использовав')
    logging.debug(guesses_made)
    logging.debug('попыток')
logging.debug('=======================================')
     


