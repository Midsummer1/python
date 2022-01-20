from abc import ABC, abstractmethod


class Stuff(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def get_consumption(self):
        pass


class Coat(Stuff):
    def __init__(self, param):
        super().__init__(param)
        print(f'Новое пальто имеет размер {self.param}')

    @property
    def get_consumption(self):
        return round(self.param / 6.5 + 0.5, 2)


class Suit(Stuff):
    def __init__(self, param):
        super().__init__(param)
        print(f'Костюм на рост {self.param}')

    @property
    def get_consumption(self):
        return round(self.param * 2 + 0.3, 2)


my_coat = Coat(48)
print(my_coat.get_consumption)
my_suit = Suit(1.87)
print(my_suit.get_consumption)
print(f'Общий расход равен: {my_coat.get_consumption + my_suit.get_consumption}')