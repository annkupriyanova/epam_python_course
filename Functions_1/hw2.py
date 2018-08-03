mmm = 0

def make_it_count(func, counter_name):

    def new_func(*args, **kwargs):
        globals()[counter_name] += 1

        return func(*args, **kwargs)

    return new_func


# def test():
#     f = make_it_count(int, 'mmm')
#
#     print(mmm)
#     print(f('10'))
#     print(mmm)
#     print(f(True))
#     print(mmm)
#
#
# if __name__ == '__main__':
#     test()
