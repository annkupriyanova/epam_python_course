import sys


def stderr_redirect(dest=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if dest:
                sys.stderr = open(dest, 'a+')
            else:
                sys.stderr = sys.stdout

            return func(*args, **kwargs)

        return wrapper
    return decorator


@stderr_redirect(dest='/Users/annakupriyanova/PycharmProjects/epam_python_course/exceptions/log.txt')
def test():
    a = 2 // 1
    return a


if __name__ == '__main__':
    print(test())
