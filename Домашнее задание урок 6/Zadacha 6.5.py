class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        super().draw()
        print('Уникальное сообщение для ручки')


class Pencil(Stationery):

    def draw(self):
        super().draw()
        print('Уникальное сообщение для карандаша')


class Handle(Stationery):

    def draw(self):
        super().draw()
        print('Уникальное сообщение для маркера')


my_pen = Pen('Ручка')
my_pencil = Pencil('Карандаш')
my_handle = Handle('Маркер')
my_pen.draw()
my_pencil.draw()
my_handle.draw()