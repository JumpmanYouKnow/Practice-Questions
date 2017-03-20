# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"


def fibonacci(n):
    m = [[1, 1],[1, 0]]
    def fib(m, n):       
        if(n == 1):
            return m
        r = fib(m, n/2)
        a, b, c, d = r[0][0], r[0][1], r[1][0], r[1][1]
        e, f, g, h= r[0][0], r[0][1], r[1][0], r[1][1]
        r[0][0], r[0][1], r[1][0], r[1][1] = a * e + b * g, a * f + b * h, c * e + d* g, c * f + d * h
        if(n % 2 == 1):
            a, b, c, d = r[0][0], r[0][1], r[1][0], r[1][1]
            e, f, g, h= 1, 1, 1, 0
            r[0][0], r[0][1], r[1][0], r[1][1] = a * e + b * g, a * f + b * h, c * e + d* g, c * f + d * h
        return r
    ans = fib(m,n)
    return ans[0][1]
