#1. Функция с двумя числами
def delenie():
    a = int(input('Введите число1: '))
    b = int(input('Введите число2: '))
    if b == 0:
        print('Число2 = 0! На ноль делить нельзя!')
    else:
        c = a / b
        return c

result = delenie()
print(result)
print()
#2. Функция с несколькими параметрами
def func1(Name, Surname, Year, City, Email, Tel):
    return print('Имя:', Name, 'Фамилия:', Surname, 'Год рождения:', Year, 'Город проживания:', City,
    'Email', Email, 'Номер телефона', Tel)
func1(Name=input('Введите имя: '), Surname=input('Введите Фамилию: '), Year=input('Введите год рождения: '),
City=input('Введите город: '), Email=input('Введите Email: '), Tel=input('Введите телефон: '))
#3. Сумма наибольших двух аргументов
def my_func(a,b,c):#задаем функцию
    list = [a, b, c]#превращаем аргументы в список
    list.sort(reverse=True)#сортируем список по убыванию
    return sum(list[:2])#находим сумму первых двух через срез
print(my_func(1, 2, 3))
#4.1 Возведение числа x в степень y чере x**y
x = float(input('Введите положительное число: '))
if x <= 0:
    x = float(input('Введите положительное число!: '))
    print('x =', x)
else:
    print('x =', x)
y = int(input('Введите отрицательное число: '))
if y >= 0:
    y = int(input('Введите отрицательное число!: '))
    print('y=',y)
else:
    print('y=',y)
def my_func(x,y):
    z = x**y
    return print(z)
my_func(x,y)
#4.2 Решение через цикл while
x = float(input('Введите положительное число: '))
if x <= 0:
    x = float(input('Введите положительное число!: '))
    print('x =', x)
else:
    print('x =', x)
y = int(input('Введите отрицательное число: '))
if y >= 0:
    y = int(input('Введите отрицательное число!: '))
    print('y=',y)
    xy = 1  # эта переменная соответствует ответу на задачу x**y
    while y < 0:  # пока y меньше 0
        xy *= 1 / x  # xy умножается на 1/x до выхода из цикла
        y += 1
    print('x в степени y =', xy)
else:
    print('y=',y)
    xy = 1 #эта переменная соответствует ответу на задачу x**y
    while y < 0: #пока y меньше 0
        xy *= 1/x #xy умножается на 1/x до выхода из цикла
        y += 1 #на каждом этапе цикла y увеличивается на 1, пока не станет равна 0(выход из цикла)
    print('x в степени y =',xy)
#5 Не понял как решать даже после объяснения на видео, слишком много уровней встроенных функций и тд
#6 Перевод в заглавную букву
def int_func(word):
    return word.capitalize()


input_string = input('Введите строку: ')
result_string_list = []
input_words = input_string.split()
for element in input_words:
    result_string_list.append(int_func(element))

print(' '.join(result_string_list))