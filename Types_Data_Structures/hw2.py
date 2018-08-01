from collections import Counter


def hw2():
    text = input("Type any text. To exit enter 'cancel'.\n")

    while text != 'cancel':
        counter = Counter(text.lower().split())
        most_common = counter.most_common()

        for (word, num) in most_common:
            if num == most_common[0][1]:
                print('{} - {}'.format(num, word))
            else:
                break

        text = input("Type any text. To exit enter 'cancel'.\n")


if __name__ == '__main__':
    hw2()
