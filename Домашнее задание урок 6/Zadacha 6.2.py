class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def square(self):
        return self._width * self._length

    def ves(self, weight_ratio, thikness):
        asphalt = self.square() * weight_ratio * thikness
        return asphalt


my_road = Road(1, 2)
print(my_road.ves(25, 1))
