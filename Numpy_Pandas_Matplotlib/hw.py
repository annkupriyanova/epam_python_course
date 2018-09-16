import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time


def matrix_mul(a, b):
    return np.matmul(a, b)


def estimate_time(matrix_a, matrix_b):
    start = time.time()
    matrix_mul(matrix_a, matrix_b)

    return time.time() - start


def estimate_complexity():
    data = []

    for n in range(2, 1001):
        a = np.random.random((n, n))
        b = np.random.random((n, n))

        t = estimate_time(a, b)

        data.append((n, t))

    df = pd.DataFrame(data, columns=['Size', 'Time'])
    df.to_csv('matrix_mul_time.csv')

    print(df)
    print('\nMean Time: {:f} sec'.format(df["Time"].mean()))
    print('Deviation: {:f} sec'.format(df["Time"].std()))

    return df


def draw_plots(df):
    # First subplot log T(log N)
    x = np.log(df['Size'][2:])
    y = np.log(df['Time'][2:])
    z = np.polyfit(x, y, 6)
    f = np.poly1d(z)
    y_new = f(x)

    plt.subplot(2, 1, 1)
    points, approx_line = plt.plot(x, y, '.', x, y_new)

    plt.xlabel('log(N)')
    plt.ylabel('log(T)')
    plt.legend([points, approx_line], ['True values', 'Approximation'], loc='lower right',
               shadow=True, fontsize='small')

    # Second subplot n(N)
    x = df['Size']
    y = np.log(df['Time']) / np.log(df['Size'])
    z = np.polyfit(x, y, 10)
    f = np.poly1d(z)
    y_new = f(x)

    plt.subplot(2, 1, 2)
    points, approx_line = plt.plot(x, y, '.', x, y_new)

    plt.xlabel('N')
    plt.ylabel('n')
    plt.legend([points, approx_line], ['True values', 'Approximation'], loc='lower right',
               shadow=True, fontsize='small')

    plt.subplots_adjust(hspace=0.4)

    plt.savefig('fig1.png')
    plt.savefig('fig1.eps')

    plt.show()


def pipeline():
    print('Creating dataset...')
    df = estimate_complexity()
    # df = pd.read_csv('matrix_mul_time.csv')
    draw_plots(df)


if __name__ == '__main__':
    pipeline()
