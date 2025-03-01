import math

numbers = [4, 5, 10, 16, 20, 21, 27, 64]

for i in numbers:
    sqr = math.sqrt(i)
    if sqr % 1 == 0:
        print(sqr)
    