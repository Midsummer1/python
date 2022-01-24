class Complex:

    def __init__(self, real, unreal):
        self.real = real
        self.unreal = unreal

    def __add__(self, other):
        return Complex(self.real + other.real, self.unreal + other.unreal)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.unreal * other.unreal, self.real * other.unreal + self.unreal * other.real)

    def __str__(self):
        return f'{self.real} + {self.unreal}j'


my_complex_number = Complex(9,5)
my_complex_number2 = Complex(-5, 1)
print(f'Сумма: {my_complex_number + my_complex_number2}')
print(f'Произведение равно: {my_complex_number * my_complex_number2}')