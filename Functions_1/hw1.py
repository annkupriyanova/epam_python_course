
def partial(func, *fixated_args, **fixated_kwargs):

    def new_func(*args, **kwargs):
        new_args = fixated_args + args

        new_kwargs = fixated_kwargs.copy()
        new_kwargs.update(kwargs)

        return func(*new_args, **new_kwargs)

    new_func.__name__ = 'partial_' + func.__name__
    new_func.__doc__ = "A partial implementation of '{}' with pre-applied arguments being: {}, {}".\
        format(func.__name__, fixated_args, fixated_kwargs)

    return new_func


# def test():
#     partial_round = partial(round, ndigits=2)
#     print('Name: ', partial_round.__name__)
#     print('Docstring: ', partial_round.__doc__)
#     print(partial_round(23.4566))
#
#
# if __name__ == '__main__':
#     test()
