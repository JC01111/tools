n = input("How many times you want to flip the coin: ")
k = input("Number of times the coin is head: ")

def calculate():
    result = int(k) / int(pow(2, int(n)))
    print("The Probability of head is", result)
    print("The Probability of tail is", 1 - result)

calculate()
