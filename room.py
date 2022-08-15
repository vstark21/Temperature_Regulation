import random
import numpy as np

class Room:

    def __init__(self, Ti, M=80, c=718, Tout=25, R=10):
        self.Tout = Tout + 273
        self.T = Ti + 273
        self.M = M
        self.c = c
        self.Req = R

    def step(self, theta):
        theta_loss = (self.T - self.Tout) / self.Req
        theta -= theta_loss
        delta_T = theta / (self.M * self.c)
        self.T += delta_T
        return self.T - 273
