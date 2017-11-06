import matplotlib.pyplot as plt
import numpy as np

def bisection_root():
    x = np.linspace(0, 1, 100)
    f = lambda z: np.sin(z)-0.5
	#ax = plt.figure((4,3)).gca()
    plt.plot(x, f(x), x, 0*x,'r--')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    ax.set_xticks(np.arange(-5, 6, 1))
    plt.grid(True)
    plt.show()
