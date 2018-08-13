import time


profile_data_dynamic = {'count': 0, 'time': 0}
profile_data_matrix = {'count': 0, 'time': 0}
profile_data_cached = {'count': 0, 'time': 0}


def profile(global_var_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            val = func(*args, **kwargs)
            globals()[global_var_name]['time'] += time.time() - start
            globals()[global_var_name]['count'] += 1

            return val
        return wrapper
    return decorator


def make_cache(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            val = func(*args)
            cache[args] = val
            return val
    return wrapper


# with cached data
@make_cache
@profile('profile_data_cached')
def fib_with_cache(n):
    if n < 2:
        return n
    return fib_with_cache(n-1) + fib_with_cache(n-2)


# dynamic implementation
@profile('profile_data_dynamic')
def fib_dynamic(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a


# with matrices
def pow(x, n, I, mult):
    """
    Возвращает x в степени n. Предполагает, что I – это единичная матрица, которая
    перемножается с mult, а n – положительное целое
    """
    if n == 0:
        return I
    elif n == 1:
        return x
    else:
        y = pow(x, n // 2, I, mult)
        y = mult(y, y)
        if n % 2:
            y = mult(x, y)
        return y


def identity_matrix(n):
    """Возвращает единичную матрицу n на n"""
    r = list(range(n))
    return [[1 if i == j else 0 for i in r] for j in r]


def matrix_multiply(A, B):
    BT = list(zip(*B))
    return [[sum(a * b
                 for a, b in zip(row_a, col_b))
            for col_b in BT]
            for row_a in A]


@profile('profile_data_matrix')
def fib_matrix(n):
    F = pow([[1, 1], [1, 0]], n, identity_matrix(2), matrix_multiply)
    return F[0][1]


def test_fibonacci_functions():
    fib_with_cache(150)
    print('Cached implementation: count={}, time={}'.format(profile_data_cached['count'], profile_data_cached['time']))

    fib_dynamic(150)
    print('Dynamic implementation: count={}, time={}'.format(profile_data_dynamic['count'], profile_data_dynamic['time']))

    fib_matrix(150)
    print('Matrix implementation: count={}, time={}'.format(profile_data_matrix['count'], profile_data_matrix['time']))

    time_dict = {'cached implementation': profile_data_cached['time'],
                 'dynamic implementation': profile_data_dynamic['time'],
                 'matrix implementation': profile_data_matrix['time']}

    min_time_elem = min(time_dict, key=time_dict.get)

    print('\nOptimal solution with execution time {} is {}.'.format(time_dict[min_time_elem], min_time_elem))


if __name__ == '__main__':
    test_fibonacci_functions()

