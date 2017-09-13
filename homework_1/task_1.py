def fibonacci(n):
    if n <= 0:
        return False
    if n == 1:
        return 1
    else:
        k = 1
        m = 0
        result = 0
        for i in range(n-1):
         result = k + m
         m = k
         k = result
        return result