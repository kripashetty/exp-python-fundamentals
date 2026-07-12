
'''
The walrus operator (:=) allows you to run an expression while simultaneously assigning the output value to a variable.
'''


import random


def get_weather():
    return random.randrange(90,150)

hot = [temp for _ in range(20) if (temp:= get_weather()) >= 100]

print (hot)