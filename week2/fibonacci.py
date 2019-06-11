# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_fast(n):
    numbers = []
    numbers.append(0)
    numbers.append(1)

    for i in range(2, n + 1):
        numbers.append(numbers[i - 1] + numbers[i - 2])
    return numbers[n]

n = int(input())
# print(calc_fib(n))
print(calc_fib_fast(n))
