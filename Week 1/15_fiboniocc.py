#  Fibonacci series up to N terms.
def fibonacci_series(n):
    a, b = 0, 1
    series = []
    while a < n:
        series.append(a)
        a, b = b, a + b
    return series
print(fibonacci_series(1000))