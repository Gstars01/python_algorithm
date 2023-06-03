import random
from time import time
time_remember = random.randrange(1,101)

for i in range(1,101):
    if i == time_remember : 
        print(i)
        break