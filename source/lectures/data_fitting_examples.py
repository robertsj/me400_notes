import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)

def scattered_points():
    n = 25
    t = np.linspace(0, 10, n)
    # measurement at time t with white noise
    y = 2*t + 3 + np.random.normal(size=n)
    plt.figure(1)
    plt.plot(t, y, 'ko')
    plt.xlabel('t')
    plt.ylabel('y(t)')
    plt.show()
    return t, y
