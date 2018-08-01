def hw3():
    text = input("Type positive integers separated by any non-digit symbols. To exit enter 'cancel'.\n")

    while text != 'cancel':
        str = [c if c.isdigit() else ' ' for c in text]
        num_lst = [int(num) for num in ''.join(str).split()]

        print(sum(num_lst))

        text = input("Type positive integers separated by any non-digit symbols. To exit enter 'cancel'.\n")


if __name__ == '__main__':
    hw3()