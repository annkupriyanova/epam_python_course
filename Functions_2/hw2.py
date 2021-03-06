def sqrt_newton(n, eps=0):
    def sqrt_helper(x=1):
        new_x = (x + n / x) / 2

        if abs(x - new_x) <= eps:
            return x
        else:
            return sqrt_helper(new_x)

    return sqrt_helper()


if __name__ == '__main__':
    print(sqrt_newton(2))
