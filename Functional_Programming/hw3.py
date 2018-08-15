def collatz_steps(n):

    def collatz(n, count=0):
        if n == 1:
            return count
        else:
            new_n = n * 3 + 1 if n % 2 else n // 2
            return collatz(new_n, count+1)

    if n > 0:
        try:
            return collatz(n)
        except RecursionError as e:
            return e.__str__()
    else:
        return 'Number must be positive.'


if __name__ == '__main__':
    print(collatz_steps(100))

