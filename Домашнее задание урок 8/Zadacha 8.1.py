class Data:
    def __init__(self, data):
        self.data = data

    def extract_data(self):
        try:
            data, mesyaz, god = self.data.split()
            return data, mesyaz, god
        except Exception as e:
            print(f'Не удалось выделить дату {e}')

    @staticmethod
    def validate_data(date_input):
        try:
            data, mesyaz, god = date_input
            if int(data) not in range(1, 32):
                raise ValueError('День указан некорректно')
            elif int(mesyaz) not in range(1, 13):
                raise ValueError('Месяц указан некорректно')
            elif int(god) not in range(0, 2028):
                raise ValueError('Год указан неверно')
        except ValueError as e:
            print(e)
        else:
            print('Валидация даты прошла успешно!!!!!!')


my_data_class = Data('23 01 2022')
my_data = my_data_class.extract_data()
print(my_data)