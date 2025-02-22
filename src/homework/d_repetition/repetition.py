#

def get_factorial(num):
    factorial = 1

    for val in range(1, num + 1):
        factorial *= val

    return factorial

def sum_odd_numbers(num):

    sum = 0
    n = 1

    while(n <= num):
        sum += n
        n += 2

    return sum