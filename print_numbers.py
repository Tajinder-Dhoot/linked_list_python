def PrintNumber(n):
    
    if n == 5:
        print(n)
        return

    print(n)
    PrintNumber(n+1)
x = 5
PrintNumber(1)