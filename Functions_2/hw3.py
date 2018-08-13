def count_points(a, b, c):
    x_coord = list(zip(a, b, c))[0]
    x_max = max(x_coord)
    x_min = min(x_coord)

    y_coord = list(zip(a, b, c))[1]
    y_max = max(y_coord)
    y_min = min(y_coord)

    sign = lambda x: 1 if x >= 0 else 0

    def count_points_helper(x, y, count=0):
        if y > y_max:
            return count_points_helper(x+1, y_min, count)
        if x > x_max:
            return count

        sign1 = sign((a[0] - x) * (b[1] - a[1]) - (b[0] - a[0]) * (a[1] - y))
        sign2 = sign((b[0] - x) * (c[1] - b[1]) - (c[0] - b[0]) * (b[1] - y))
        sign3 = sign((c[0] - x) * (a[1] - c[1]) - (a[0] - c[0]) * (c[1] - y))

        if sign1 == sign2 == sign3:
            count += 1

        return count_points_helper(x, y+1, count)

    return count_points_helper(x_min, y_min)


if __name__ == '__main__':
    print(count_points((0,0),(2,0),(0,2)))
