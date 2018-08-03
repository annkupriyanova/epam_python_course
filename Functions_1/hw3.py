def atom(init_val=None):
    value = init_val

    def get_value():
        return value

    def set_value(val):
        nonlocal value
        value = val

        return value

    def process_value(*args):
        for f in args:
            set_value(f(value))

        return value

    return get_value, set_value, process_value


# def test():
#     f1 = lambda x: x*3
#     f2 = lambda x: x**2
#
#     get_val, set_val, proc_val = atom(1)
#
#     print(get_val())
#     print(proc_val(f1, f2))
#     print(set_val(2))
#     print(get_val())
#
#
# if __name__ == '__main__':
#     test()