def hw5():
    sum_palindrom = 0

    for num in range(1000000):
        if is_palindrom_decimal(num) and is_palindrom_binary(num):
            sum_palindrom += num
            print(num, '-', bin(num)[2:])

    print('\nThe sum of palindrom numbers is {}'.format(sum_palindrom))


def is_palindrom_decimal(dec_number):
    temp = dec_number
    reverse = 0

    while temp != 0:
        reverse = (reverse * 10) + (temp % 10)
        temp = temp // 10

    return dec_number == reverse


def is_palindrom_binary(dec_number):
    binary = bin(dec_number)
    binary = binary[2:]

    return binary == binary[::-1]


if __name__ == '__main__':
    hw5()
