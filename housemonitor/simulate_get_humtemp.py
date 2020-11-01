from random import random
import math 

def get_humtemp():
    temp = 20.0 + (random()-0.5)*30.
    humidity = (1.+math.cos(temp/20.))*49.
    return (temp, humidity)