class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} {self.color} цвета ехала со скоростью {self.speed}')

    def stop(self):
        print(f'Машина {self.name} {self.color} цвета остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} {self.color} цвета повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость машины: {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости!')
        else:
            Car.show_speed(self)


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 300:
            print('Превышение скорости')
        else: Car.show_speed(self)


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)

my_police_car = PoliceCar(90, 'черный', 'Жигуль')
my_police_car.go()
my_police_car.turn('налево')
my_police_car.stop()
my_police_car.show_speed()
print()
my_work_car = WorkCar(30, 'Желтый', 'самосвал', False)
my_work_car.go()
my_work_car.turn('направо')
my_work_car.stop()
my_work_car.show_speed()