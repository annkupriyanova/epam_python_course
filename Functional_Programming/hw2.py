from functools import reduce


def is_armstrong(number):
    num_str = str(number)
    digits = list(map(lambda x: int(x)**len(num_str), num_str))

    if number == reduce(lambda x, y: x + y, digits):
        return 'Число Армстронга'
    else:
        return 'Не число Армстронга'


if __name__ == '__main__':
    print(is_armstrong(0))
