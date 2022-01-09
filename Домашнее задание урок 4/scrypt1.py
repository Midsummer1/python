from sys import argv
script_name, productivity, rate_per_hour, bonus = argv
print('Name', script_name)
print('productivity:', productivity)
print('rate:', rate_per_hour)
print('Bonus', bonus)
print('salary:', int(productivity) * int(rate_per_hour) + int(bonus))