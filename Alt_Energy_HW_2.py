""" This is a homework question for the ECE 5374 Class at Virginia Tech.
Its purpose is to use SciPi to integrate a simple wind distribution function for a given set of data
"""
#basic integration function
from scipy import integrate

V_R = 12.5
V_C = 6.26
K = input("Input k: ")
C = input("Input C: ")

g13 = lambda x: (x**3 - V_C**3)*(K/C)*((x/C)**(K-1))*math.exp(-((x/C)**K))

result = integrate.quad(g13, V_C , V_R)

return result
