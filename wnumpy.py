#!/usr/bin/env python
import numpy


def everything(rs, xs, count):
    for i in range(count):
        xs = rs * xs * (1 - xs)
    return rs, xs

if __name__ == "__main__":
    rs = 2 + 2 * numpy.random.random((500, 200))
    xs = numpy.random.random((500, 200))
    import time

    started = time.time()
    rs, xs = everything(rs, xs, 2000)
    print "steps/s", 500 * 200 * 2000 / (time.time() - started)
    from matplotlib import pyplot as plt
    plt.scatter(rs, xs)
    plt.show()
