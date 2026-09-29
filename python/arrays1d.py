import random

array_length = 10
lowest = 1
highest = 100

array = []
for counter in range(array_length):
    array.append(random.randint(lowest, highest))

print(array)
