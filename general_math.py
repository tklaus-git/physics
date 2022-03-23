

import numpy as np 
from general_math import *


G = 6.67408*(10**(-11))

'''

'''
class Celestial:
    def __init__(self, m, point):
        self.m = m
        self.p = point


def gravity(b1, b2):
    return (b1.m * b2.m*G)/((distance(b1.p, b2.p))**2)

