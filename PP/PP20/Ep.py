def Ep(x):
    ell0 = 5
    d = 3.4
    shift = 2**0.5
    k = 3500
    return 0.5 * k * ((d**2 + (x+shift)**2)**0.5 - ell0)**2

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    
    x = np.linspace(-10,10,1000)
    plt.plot(x,Ep(x))
    plt.show()
