import matplotlib.pyplot as plt
import numpy as np

def bisection_root():
    
    f = lambda z: np.sin(z)-0.4    
    x = np.linspace(0, 1, 100)    
    plt.plot(x, f(x), 'k', x, 0*x,'k--')
    
    # Plot f(A), f(B)
    A, B, C = 0, 1.0, 0.5
    plt.plot(A, f(A), 'bs', ms=22)
    plt.plot(B, f(B), 'bs', ms=22)
    plt.plot(C, f(C), 'bs', ms=22, label='initial')
    plt.fill_betweenx([f(A), f(B)], A, B, color='b', alpha=0.05)
    
    A, B, C = A, C, (A+C)/2
    plt.plot(A, f(A), 'ro', ms=15)
    plt.plot(B, f(B), 'ro', ms=15)
    plt.plot(C, f(C), 'ro', ms=15, label='after first iteration')
    plt.fill_betweenx([f(A), f(B)], A, B, color='r', alpha=0.1)
    
    A, B, C = C, B, (C+B)/2
    plt.plot(A, f(A), 'c>', ms=12)
    plt.plot(B, f(B), 'c>', ms=12)
    plt.plot(C, f(C), 'c>', ms=12, label='after second iteration')
    plt.fill_betweenx([f(A), f(B)], A, B, color='c', alpha=0.15)
    
    
    plt.legend(fontsize=12)
    plt.xlabel('$x$', fontsize=16)
    plt.ylabel('$f(x)$', fontsize=16)
    plt.show()
 


def fun(x) :
    return (np.sin(x**2)-3)**2

def extrema():
    import sympy

    x = sympy.Symbol('x')
    f = x*(x-10)*(x+8)**2/1000
    x0, x1, x2 = sympy.solve(sympy.diff(f, x))
    z = np.linspace(-15, 15, 1000)
    fun = sympy.lambdify(x, f)
    plt.figure(3)
    plt.plot(z, fun(z), 'k-', x0, fun(x0), 'bo', x1, fun(x1), 'rs', 
             x2, fun(x2), 'g*', markersize=20)
    plt.ylim(-10,10)
    plt.grid(True)        
    plt.title('Various extrema')
    plt.show()
