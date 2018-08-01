def hw1():
    text = input("Type any text:\n")
    text_set = set(text.split())
    print(' '.join(text_set))


if __name__ == '__main__':
    hw1()