import numpy as np

class PID:
    def __init__(self, kp=0, ki=0, kd=0):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.last_error = 0
        self.integral = 0

    def step(self, error, dt=1):
        self.integral = self.integral + error * dt
        self.derivative = (error - self.last_error) / dt
        self.last_error = error
        return self.kp * error + self.ki * self.integral + self.kd * self.derivative

    def reset(self):
        self.last_error = 0
        self.integral = 0
