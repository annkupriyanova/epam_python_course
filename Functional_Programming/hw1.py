from functools import reduce


def hw1():
    summa = sum(x**2 for x in range(10**3))
    print(summa)

    summa2 = sum(map(lambda x: x**2, range(10**3)))
    print(summa2)

    lst = range(10**3)
    summa3 = reduce((lambda x,y: x + y*y), lst)
    print(summa3)


if __name__ == '__main__':
    hw1()
