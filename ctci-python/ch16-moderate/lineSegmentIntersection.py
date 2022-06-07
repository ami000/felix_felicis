def line_intersection(line1, line2):
    print(line1, line2)
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    print(xdiff)
    print(ydiff)

    div = det(xdiff, ydiff)
    print(div)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

if __name__ == '__main__':
    l1 = [(1, 25), (31, 60)]
    l2 = [(1, 89), (15, 30)]

    print(line_intersection(l1, l2))
