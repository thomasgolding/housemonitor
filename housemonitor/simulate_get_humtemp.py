import math
from random import random


def get_humtemp():
    temp = 20.0 + (random() - 0.5) * 30.0
    humidity = (1.0 + math.cos(temp / 20.0)) * 49.0
    return (temp, humidity)
