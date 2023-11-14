import math
import random

class Intervalle_net() : 
    def __init__(self, a1, a2) :
        self.a1 = a1
        self.a2 = a2
    
    def __str__(self) :
        return "[" + str(self.a1) + ", " + str(self.a2) + "]"

    def __add__(self, other) :
        return Intervalle_net(self.a1 + other.a1, self.a2 + other.a2)

    def __neg__(self) :
        return Intervalle_net(-self.a2, -self.a1)

    def __sub__(self, other) :
        return self + (-other)

    def __mul__(self, other) :
        return Intervalle_net(max([self.a1 * other.b1, self.a1 * other.b2, self.a2 * other.b1, self.a2 * other.b2]), 
                              max([self.b1 * other.a1, self.b1 * other.a2, self.b2 * other.a1, self.b2 * other.a2]))