import time


def make_cache(timeout=100):
    def decorator(func):
        cache = {}

        def wrapper(*args):
            nonlocal cache
            cache = {k: v for k, v in cache.items() if v[1] > time.time()}

            if args in cache:
                val, _ = cache[args]
            else:
                val = func(*args)
                expire = time.time() + timeout
                cache[args] = (val, expire)

            return val
        return wrapper
    return decorator


@make_cache(50)
def slow_function(*args):
    time.sleep(30)
    return args


# def test():
#     slow_function('function call 0')
#     slow_function('function call 1')
#     slow_function('function call 2')
#
#
# if __name__ == '__main__':
#     test()
