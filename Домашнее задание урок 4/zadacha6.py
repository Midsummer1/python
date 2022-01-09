from itertools import count, cycle

def generator1(start_from):
    for el in count(start_from):
        if el > 10:
            break
        yield el

for el in generator1(3):
    print(el)

list = '12345'
print(f'Элементы списка для повторения: {list}')
c = 0

for el in cycle(list):
    if el == list[0]:
        c += 1
    if c > 2:
        break
    else:
        print(el)