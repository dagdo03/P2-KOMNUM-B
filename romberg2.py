import numpy as np
from scipy import integrate 
f = lambda x: x * np.sin(x) #integral of x * sin(x)
a = 0
b = np.pi/2

romberg = integrate.romberg(f, a, b, show = True)