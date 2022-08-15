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
    # [0.6 * kcr, 1.2 * (kcr / pcr), 0.075 * (kcr * pcr)],
]
labels = [
    "Kp: 0.25 * Kcr, Ki: 0, Kd: 0",
    "Kp: 0.45 * Kcr, Ki: 0.54 * (Kcr / Pcr), Kd: 0",
    "Kp: 0.2 * Kcr, Ki: 0.4 * (Kcr / Pcr), Kd: 0.066 * (Kcr * Pcr)",
    # "Kp: 0.6 * Kcr, Ki: 1.2 * (Kcr / Pcr), Kd: 0.075 * (Kcr * Pcr)",
]

for kp, ki, kd in values:
    controller = PID(kp=kp, ki=ki, kd=kd)

    current_temp = 75
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

    plt.plot(temps, label=labels.pop(0))

plt.plot(np.ones(50) * target_temp, label="Target Setpoint")
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.show()