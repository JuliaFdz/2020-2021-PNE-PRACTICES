def fibonaccisum(n):
    x = 0
    y = 1
    fibonacci_list = [x,y]
    for e in range(0,n-1):
        fb = x + y
        fibonacci_list.append(fb)
        x = y
        y = fb
    return fibonacci_list

print('Sum of the first 5 fibonacci series: ', sum(fibonaccisum(5)))
print('Sum of the first 10 Fibonacci Series: ', sum(fibonaccisum(10)))
