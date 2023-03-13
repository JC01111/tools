import math

N = int(input("what's the total number of N: "))
n = int(input("Number of n you choose: "))
G = int(input("what's the total number of good G: "))
g = int(input("Number of good g you choose: "))
B = N - G
b = n - g

def ask():
    a = int(input("'1' to continue, '2' to exit, '3' for new: "))
    if a == 1:
        hypergeometric2()
    elif a == 2:
        return
    elif a == 3:
        hypergeometric3()

def hypergeometric():
    print(round((math.comb(G, g) * math.comb(B, b)) / math.comb(N, n) , 4))
    print("\n")
    ask()


# Continue with previous data
def hypergeometric2():
    g = int(input("Number of good g you choose: "))
    b = n - g
    print(round((math.comb(G, g) * math.comb(B, b)) / math.comb(N, n) , 4))
    print("\n")
    ask()


# New input inside the function
def hypergeometric3():
    # Input
    N = int(input("what's the total number of N: "))
    n = int(input("Number of n you choose: "))
    G = int(input("what's the total number of good G: "))
    g = int(input("Number of good g you choose: "))
    B = N - G
    b = n - g

    print(round((math.comb(G, g) * math.comb(B, b)) / math.comb(N, n) , 4))
    print("\n")
    ask()


hypergeometric()
