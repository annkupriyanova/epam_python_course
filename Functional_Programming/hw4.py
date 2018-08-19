import math
from functools import reduce
from operator import mul


def problem9():
    res = [a*b*c for b in range(2, 501) for a in range(1, b) for c in [math.sqrt(a**2+b**2)] if a+b+c == 1000]
    return int(res[0])


def problem6():
    return sum(range(101))**2 - sum(x**2 for x in range(101))


def problem48():
    return str(sum(x**x for x in range(1, 1001)))[-10:]


def problem40():
    fraction = "".join(str(i) for i in range(1, 1000000))
    return reduce(mul, (int(fraction[10**i - 1]) for i in range(7)))


if __name__ == '__main__':
    print('Problem 9: {}'.format(problem9()))
    print('Problem 6: {}'.format(problem6()))
    print('Problem 48: {}'.format(problem48()))
    print('Problem 40: {}'.format(problem40()))
