import numpy as np
from pid import PID
from room import Room
import matplotlib.pyplot as plt

kcr = 114880
pcr = 2
values = [
    [0.25 * kcr, 0, 0],
    [0.45 * kcr, 0.54 * (kcr / pcr), 0],
    [0.2 * kcr, 0.4 * (kcr / pcr), 0.066 * (kcr * pcr)],
]

for kp, ki, kd in values:
    controller = PID(kp=kp, ki=ki, kd=kd)

    current_temp = 25
    target_temp = 50
    threshold = 1e-2

    room = Room(Ti=current_temp)

    errors = []
    temps = []
    converge_point = []

    for i in range(50):
        
        temps.append(current_temp)
        error = target_temp - current_temp
        errors.append(error)

        if abs(error) < threshold and not converge_point:
            converge_point.append([i, current_temp])

        theta = controller.step(error)
        current_temp = room.step(theta)

    plt.plot(temps, label=f"kp: {kp}, ki: {ki}, kd: {kd}")

plt.legend()
plt.show()