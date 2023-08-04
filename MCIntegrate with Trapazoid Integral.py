# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 21:44:35 2023

@author: rjfch
"""

from random import random
from numpy import linspace

def trapezoid_integral(f, a, b, n):
    x = linspace(a, b, num=n, endpoint=True)
    h = (b - a) / n
    integral = 0
    for i in range(1, n):
        integral += (f(x[i-1]) + f(x[i])) * h / 2
    return integral

def MCintegrate(f, a, b, n):
    x = linspace(a, b, num=n, endpoint=True)
    maxF = max(f(x))
    area = 0
    for i in range(n):
        randNoX = random() * (b - a) + a
        randNoY = random() * maxF
        if randNoY <= f(randNoX):
            area += 1
    boxArea = (b - a) * maxF
    integral = area / n * boxArea
    return integral

if __name__ == "__main__":
    def f(x):
        return x**2

    # Perform the Monte Carlo integration
    area = MCintegrate(f, 1.0, 3.0, 50)

    # Perform the trapezoid integral
    trapezoid_area = trapezoid_integral(f, 1.0, 3.0, 50)

    print("Monte Carlo Integral:", area)
    print("Trapezoid Integral:", trapezoid_area)