first_list = [el for el in range(100, 1001) if el %2 == 0]
print(first_list)
from functools import reduce
umn = reduce(lambda x,y: x * y, first_list)
print(umn)