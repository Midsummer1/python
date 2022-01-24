class ErrDivision(Exception):
    def __init__(self):
        self.txt = 'My division by zero'


def division(divident, divisor):
    try:
        if divisor == 0:
            raise ErrDivision
        print(divident / divisor)
    except ErrDivision as err:
        print(err.txt)

division(5, 0)