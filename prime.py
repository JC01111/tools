n = int(input("What's your n: "))

def prime(n, k):
    if (n % k == 0) and (k != 1) and (k != n):
        print("Not Prime")
        return
    elif k == n and k != 1:
        print("prime")
        return
    else:
        prime(n , k + 1)

prime(n, 1)
