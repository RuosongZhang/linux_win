def countdown(s,n):
    if n <= 0:
        return
    print(s)
    print(n)
    countdown(s,n-1)
countdown(100,100)