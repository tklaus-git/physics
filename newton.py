from tkinter import Y
import numpy as np 
from general_math import *


G = 6.67408*(10**(-11))

'''

'''
class Celestial:
    def __init__(self, name, m, point, v):
        self.name = name
        self.m = m
        self.p = point
        self.v = v
    def motion(self, bodies):
        forces = []
        t_force = [0, 0]
        m = 1 # shifting x and y 
        for body in bodies:
            if body.name != self.name:
                # Gravitational force
                F = gravity(self, body)

                # Get vector from self to point, and make magnitude equal to gravitational force.
                shifted = [body.x- self.x, body.y - self.y]
                m = (F**2)/(shifted[0]**2 + shifted[1]**2)
                # shift
                shifted[0] *= m
                shifted[1] *= m

                forces.append(shifted)
        # Add all force vectors, resulting in one
        for f in forces:
            t_force[0] += f[0]
            t_force[1] += f[1]

        # Force to acceleration:
        a = t_force/self.m

        # acceleration to velocity
        vc = a*2.5*10**6# Velocity change
        
        # Changing position according to
        # Normalizing, can possibly skip to this step earlier
        m = (vc**2)/(F[0]**2 + F[1]**2) # shift
        shifted[0] *= m
        shifted[1] *= m
           
        



        # Get velocity after a certain amount of time

        # Move to apropriate place


        return


def gravity(b1, b2):
    return (b1.m * b2.m*G)/((distance(b1.p, b2.p))**2)

sun = Celestial('sun', 2*10**30, Point(0,0))
earth = Celestial('earth', 6*10**24, Point(0,15*10**10))

# bodies = [sun, earth]

# print(gravity(sun, earth))



