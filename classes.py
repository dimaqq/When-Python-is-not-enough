#!/usr/bin/env python


class Point:
    def __init__(self, x):
        self.x = x

    def step(self, r):
        self.x = r * self.x * (1 - self.x)

    def stepx(self, r, count):
        for i in range(count):
            self.step(r)


def everything(rs, xs, count):
    for r in rs:
        for x in xs:
            point = Point(x)
            point.stepx(r, count)
            yield (r, point.x)

if __name__ == "__main__":
    import random
    rs = [2 + 2 * random.random() for i in range(100)]
    xs = [random.random() for i in range(100)]
    import svg
    import time
    started = time.time()
    with open("test.svg", "w") as fout:
        for line in svg.draw(everything(sorted(rs), sorted(xs), 2000)):
            print >> fout, line
    print "steps/s", 100 * 100 * 2000 / (time.time() - started)

