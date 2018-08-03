from multimethod import multimethod


@multimethod
def letters_range(start: str, stop: str, step=1):
    letters = []

    start_i = ord(start)
    stop_i = ord(stop)

    for i in range(start_i, stop_i, step):
        letters.append(chr(i))

    return letters


@multimethod
def letters_range(stop: str):
    letters = []

    start_i = ord('a') if stop.islower() else ord('A')
    stop_i = ord(stop)

    for i in range(start_i, stop_i, 1):
        letters.append(chr(i))

    return letters


# def test():
#     print(letters_range('p', 'g', -2))
#
#
# if __name__ == '__main__':
#     test()
