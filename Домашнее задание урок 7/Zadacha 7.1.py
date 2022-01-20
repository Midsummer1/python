class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        my_str = '\n'
        for row in self.matrix:
            for el in row:
                my_str += f'{el:>10}'
            my_str += '\n'
        return my_str

    def __add__(self, other):
        add = []
        if len(self.matrix) != len(other.matrix):
            print('Please check matrixes dimensions')
            return
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(other.matrix[i]):
                print('Please check matrixes dimensions')
                return
            row = []
            for j in range(len(self.matrix[i])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            add.append(row)
        return Matrix(add)


my_m1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f'mu_m1 = {my_m1}')
my_m2 = Matrix([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]])
print(f'my_m2 = {my_m2}')
print(f'my_m1 + my_m2 = {my_m1 + my_m2}')