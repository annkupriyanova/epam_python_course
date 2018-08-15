def count_points(a, b, c):
    x_coord = list(zip(a, b, c))[0]
    x_max = max(x_coord)
    x_min = min(x_coord)

    y_coord = list(zip(a, b, c))[1]
    y_max = max(y_coord)
    y_min = min(y_coord)

    def count_points_helper(x, y, count=0):
        if y > y_max:
            return count_points_helper(x+1, y_min, count)
        if x > x_max:
            return count

        summa = square(x, y, a[0], a[1], b[0], b[1]) + square(x, y, b[0], b[1], c[0], c[1]) \
            + square(x, y, c[0], c[1], a[0], a[1])

        if summa == square(a[0], a[1], b[0], b[1], c[0], c[1]):
            count += 1

        return count_points_helper(x, y+1, count)

    return count_points_helper(x_min, y_min)


def square(ax, ay, bx, by, cx, cy):
    return abs(bx*cy - cx*by - ax*cy + cx*ay + ax*by - bx*ay)


if __name__ == '__main__':
    print(count_points((-2, -5), (0, 0), (5, 2)))
    print(count_points((5, 2), (0, 0), (-2, -5)))
    print(count_points((5, 2), (-2, -5), (0, 0)))
