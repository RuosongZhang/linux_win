def fibonacci(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers')
    
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers')
        return None
    elif n == 0:
        return 1
    else:
        return n + fibonacci(n-2)
ax = fibonacci(4)
print(ax)