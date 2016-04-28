def factorial(n):
    if n < 0:
        raise ValueError('n can\'t be less than 0')
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
