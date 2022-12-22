import math
from scipy import integrate 

function = input("Masukkan Fungsi : ")

def f(x):
    f = eval(function)
    return f

a = float(input("Masukkan batas bawah : "))
b = float(input("Masukkan batas atas : "))

romberg = integrate.romberg(f, a, b, show = True) 
