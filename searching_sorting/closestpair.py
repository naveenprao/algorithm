import random
# import numpy as np
import pylab as pl
import operator
import sys
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '%d,%d' % (self.x, self.y)

def square_of_distance(p, q):
    return math.sqrt(math.pow((p.x-q.x), 2) + math.pow((p.y-q.y), 2))

def closest_pair(points):
    points_by_x = sorted(points, key=operator.attrgetter('x'))
    points_by_y = sorted(points, key=operator.attrgetter('y'))

    def _testpair(p, q):
        d = square_of_distance(p, q)
        if d < best[0]:
            best[0] = d
            best[1] = (p, q)

    def _sort_by_y(first, last):
        points_by_y = points_by_x[first:last+1]
        points_by_y.sort(key=operator.attrgetter('y'))
        return points_by_y

    def _closest_pair(first, last):
        if first == last:
            return

        mid = (first+last)/2
        _closest_pair(first, mid)
        _closest_pair(mid+1, last)

        split_point = points_by_x[mid]
        left_limit = split_point.x - math.sqrt(best[0])
        right_limit = split_point.x + math.sqrt(best[0])
        candidate_points = filter(lambda pt: left_limit <= pt.x <= right_limit, points_by_y)
        # candidate_points = filter(lambda pt: left_limit <= pt.x <= right_limit, points_by_x[first:last+1])
        # candidate_points.sort(key=operator.attrgetter('y'))
        print 'candidate points'
        for c in candidate_points:
            print c
        print 'delta: %d' % math.sqrt(best[0])

        for idx in range(len(candidate_points)-1):
            j = idx+1
            while j < len(candidate_points) and j < 8:
                _testpair(candidate_points[idx], candidate_points[j])
                j += 1

    if len(points) < 2:
        return 0, None

    if len(points) == 2:
        return square_of_distance(points[0], points[1])

    #initialize
    best = [square_of_distance(points_by_x[0], points_by_x[1]), (points_by_x[0], points_by_x[1])]
    _closest_pair(0, len(points)-1)
    return best[0], best[1]

if __name__ == '__main__':
    # x_co = random.sample(range(0, 100), 20)
    # y_co = random.sample(range(0, 100), 20)
    #
    # points = [None]*10
    # for i in range(10):
    #     points[i] = Point(x_co[i], y_co[i])
    #
    # length, pts = closest_pair(points)
    # print length
    # for p in pts:
    #     print p

    # pl.plot(x_co, y_co, 'ro')
    # pl.show()

    sample_data = [(0, 0), (7, 6), (2, 20), (12, 5), (16, 16), (5, 8), (19, 7), (14, 22), (8, 19), (7, 29), (10, 11),
                   (1, 13)]
    sample_point, sample_x, sample_y = [], [], []
    for tup in sample_data:
        sample_point.append(Point(tup[0], tup[1]))
        sample_x.append(tup[0])
        sample_y.append(tup[1])

    lt, pair = closest_pair(sample_point)
    print lt
    for p in pair:
        print p

    pl.plot(sample_x, sample_y, 'ro')
    pl.show()
