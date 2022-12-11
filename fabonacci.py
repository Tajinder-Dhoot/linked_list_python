def Fibo(n):
    """
    Gives nth element of the fibonacci series
    """

    if(n < 2):
        return n

    return Fibo(n-1) + Fibo(n-2)

print(Fibo(50))