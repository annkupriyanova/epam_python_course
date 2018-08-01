
def hw4():
    text = input("Type positive integers separated by spaces. To exit enter 'cancel'.\n")

    while text != 'cancel':
        numbers = [int(num) for num in text.split()]

        if numbers:
            print(min_exclusive_num(numbers))

        text = input("Type positive integers separated by spaces. To exit enter 'cancel'.\n")


def min_exclusive_num(numbers):
    """
     Complexity --> O(n). Algorithm passes through n numbers 2 times.
    """
    n = len(numbers)
    checks = [False]*n

    for num in numbers:
        if num <= n:
            checks[num-1] = True

    for i, check in enumerate(checks):
        if not check:
            return i+1

    return n + 1


if __name__ == '__main__':
    hw4()
