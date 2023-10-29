# Efficientily compute a fibonacci sequence

def fibonacci(n):
    res = []
    memo = {}
    def calc_fib(n, memo):
        if n == 0 or n == 1:
            return n
        else:
            if n not in memo:
                return calc_fib(n-2, memo) + calc_fib(n-1, memo)
            else:
                return memo[n]
    
    for num in range(n+1):
        res.append(calc_fib(num, memo))
    
    return res

def fib_second(n):
    res = []
    one, two = 1, 1
    for i in range(1, n + 1):
        if i == 1 or i == 2:
            res.append(one)
        else:
            temp = one
            one = two
            two = one + temp
            res.append(two)
    return res


print(fib_second(10))
