def mean_abs_error(e):
    """Mean, absolute error."""
    v = 0
    for i in range(len(e)) :
        v += abs(e[i])
    return v/len(e)
        
def rms_error(e) :
    """Root-mean-square error."""
    v = 0
    for i in range(len(e)) :
        v += e[i]**2
    return v**0.5
        
def max_abs_error(e) :
    """Maximum, absolute error."""
    v = 0
    for i in range(len(e)) :
        if abs(e[i]) > v:
            v = abs(e[i])
    return v

pi = 1.618033988749895
