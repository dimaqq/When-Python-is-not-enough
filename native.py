#!/usr/bin/env python

#def stepx(r, x, count):
#    for i in range(count):
#        x = r * x * (1 - x)
#    return x


def everything(rs, xs, count):
    for r in rs:
        for x in xs:
            #x = stepx(r, x, count)
            for i in range(count):
                x = r * x * (1 - x)
            yield (r, x)

if __name__ == "__main__":
    import random
    rs = [2 + 2 * random.random() for i in range(500)]
    xs = [random.random() for i in range(200)]
    import svg
    import time
    started = time.time()
    with open("test.svg", "w") as fout:
        for line in svg.draw(everything(sorted(rs), sorted(xs), 2000)):
            print >> fout, line
    print "steps/s", 500 * 200 * 2000 / (time.time() - started)
