from itertools import cycle
from time import sleep

class Trafficlight:
    color_1 = ('красный', 'желтый', 'зеленый')
    time_1 = (7, 2, 5)
    message = ('красный', 'желтый', 'зеленый')

    def __init__(self, color):
        self.__color = color
    def running(self):
        my_cycle = cycle(self.color_1)
        for traffic_color in my_cycle:
            if self.__color == traffic_color:
                print(self.message[self.color_1.index(self.__color)])
                sleep(self.time_1[self.color_1.index(self.__color)])
                self.__color = next(my_cycle)
my_traffic = Trafficlight('красный')
my_traffic.running()