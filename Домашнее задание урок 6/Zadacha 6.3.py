class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


my_position = Position('Иван', 'Иванов', 'золотокопатель', 500, 30)
print(f'Полная зарплата {my_position.get_full_name()} равняется {my_position.get_total_income()} киллограмм золота в день')