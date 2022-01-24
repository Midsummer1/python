class OwnException(Exception):
    def __init__(self):
        self.txt = "Некорректный тип данных!"

mylist = []
input_string = input('Введите число для выхода введите пустую строку: ')
while input_string:
    try:
        if input_string.isdigit():
            mylist.append(float(input_string))
        else:
            raise OwnException
    except OwnException as e:
        print(e.txt)

    input_string = input('Введите число для выхода введите пустую строку: ')

print(mylist)