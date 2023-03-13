import math
import numpy as np

ask = input("Enter '1' for Binomial, '2' for Poisson, '3' to exit:")

def Binomial():
    if int(ask) == 1:
        # Binomial Distribution
        input1 = input("What's the n:")
        input2 = input("What's the Probability:")
        input3 = input("What's the k: ")
        n = int(input1)
        p = float(input2)
        k = int(input3)
        result = round((math.factorial(n) / (math.factorial(k) * math.factorial(n-k))) * float(p**k) * (float(1-p) ** (n-k)), 4)
        print(result)
        print("\n")
        Binomial()
    elif int(ask) == 3:
        return
    else:
        # Poission
        input1 = input("What's the n:")
        input2 = input("What's the Probability:")
        input3 = input("What's the k: ")
        n = int(input1)
        p = float(input2)
        k = int(input3)
        mean = n*p
        result = round((math.e ** (-mean)) * (mean ** k) / math.factorial(k), 4)
        print(result)
        print("\n")
        Binomial()

Binomial()

# Notes
"""
How to convert ^ to power
"""
