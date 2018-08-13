def hw1():
    text = input("Type any text. To exit enter 'cancel'.\n")

    while text != 'cancel':
        text_to_number(text)
        text = input("Type any text. To exit enter 'cancel'.\n")
    print('Bye!')


def text_to_number(text):
    if text_is_number(text):
        number = int(text)
        print(number * 3 + 1 if number % 2 else number // 2)
    else:
        print("Can't transform the text into a number.")


def text_is_number(text):
    if len(text) == 0:
        return True
    elif not text[0].isdigit():
        return False
    return text_is_number(text[1:])


if __name__ == '__main__':
    hw1()