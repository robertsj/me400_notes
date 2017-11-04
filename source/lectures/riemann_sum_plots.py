import matplotlib.pyplot as plt
import numpy as np

 

def right_sided_sum():
    plt.figure(1)
    x = np.linspace(0, 1, 10000)
    y = x**2
    xr = np.array([0, .2, .2000, .4, .40000, .6, .60000, .8, .80000, 1.])
    yr = np.array([.2**2, .2**2, .4**2, .4**2, .6**2, .6**2, .8**2,.8**2, 1., 1.])
    xrr = np.array([.2,.4,.6,.8,1.])
    yrr = xrr**2
    plt.plot(x, y, 'k-', xr, yr, 'k--', xrr, yrr, 'ko', markersize=10)
    yr2=np.interp(x, xr, yr)
    plt.fill_between(x, yr2, y, where=yr2 >= y, facecolor='green', interpolate=True, alpha=0.4)
    plt.fill_between(x, y, 0*x, where= y>=0*x, facecolor='blue', interpolate=True, alpha=0.4)
    plt.ylim((0, 1.2))
    plt.grid(True)
    plt.title('Right-Sided Sum')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.show()

def left_sided_sum():
    plt.figure(2)
    x = np.linspace(0, 1, 10000)
    y = x**2
    xl = np.array([0, .2, .2, .4, .4, .6, .6, .8, .8, 1.])
    yl = np.array([0.0, 0.0, .2**2, .2**2, .4**2, .4**2, .6**2, .6**2, .8**2,.8**2])
    xll = np.array([0, .2, .4, .6, .8])
    yll = xll**2
    plt.plot(x, y, 'k-', xl, yl, 'k--', xll, yll, 'ko', markersize=10)
    yl2=np.interp(x, xl, yl)
    plt.fill_between(x, y, yl2, where= y>=yl2, facecolor='red', interpolate=True, alpha=0.4)
    plt.fill_between(x, yl2, 0*yl2, where=yl2 >= 0*y, facecolor='blue', interpolate=True, alpha=0.4)
    plt.ylim((0, 1.2))
    plt.grid(True)
    plt.title('Left-Sided Sum')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.show()

def midpoint_sum():
    plt.figure(3)
    x = np.linspace(0, 1, 10000)
    y = x**2
    xm = np.array([0, .2, .2, .4, .4, .6, .6, .8, .8, 1.])
    ym = np.array([0.1**2, 0.1**2, .3**2, .3**2, .5**2, .5**2, .7**2, .7**2, .9**2,.9**2])
    xmm = np.array([0.1, .3, .5, .7, .9])
    ymm = xmm**2
    ym2=np.interp(x, xm, ym)
    plt.fill_between(x, ym2, y, where=ym2 > y, facecolor='green', interpolate=True, alpha=0.4)
    plt.fill_between(x, ym2, y, where=ym2 < y, facecolor='red', interpolate=True, alpha=0.4)
    plt.fill_between(x, np.minimum(ym2, y), x*0, where=np.minimum(ym2, y)>x*0, facecolor='blue', interpolate=True, alpha=0.4)
    plt.plot(x, y, 'k-', xm, ym, 'k--', xmm, ymm, 'ko', markersize=10)
    plt.ylim((0, 1.2))
    plt.grid(True)
    plt.title('Midpoint Sum')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.show()

def trapezoid_rule():
    plt.figure(3)
    x = np.linspace(0, 1, 10000)
    y = x**2
    xm = np.array([0,  .2,  .4, .6, .8, 1.])
    ym = xm**2
    ym2=np.interp(x, xm, ym)
    plt.fill_between(x, ym2, y, where=ym2 > y, facecolor='green', interpolate=True, alpha=0.4)
    plt.fill_between(x, ym2, y, where=ym2 < y, facecolor='red', interpolate=True, alpha=0.4)
    plt.fill_between(x, np.minimum(ym2, y), x*0, where=np.minimum(ym2, y)>x*0, facecolor='blue', interpolate=True, alpha=0.4)
    plt.plot(x, y, 'k-', xm, ym, 'k--', markersize=10)
    plt.ylim((0, 1.2))
    plt.grid(True)
    plt.title('Trapezoid Rule')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.show()



