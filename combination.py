from factorial import factorial
def comb(n,k):
    if(k>n):
        raise ValueError("k should be smaller or equal to n")
    if(k<0):
        raise ValueError("n and k can't be negative")
    if(n!=int(n) or k!=int(k)):
        raise TypeError("n and k should be integers")
    return factorial(n)/(factorial(k)*factorial(n-k))