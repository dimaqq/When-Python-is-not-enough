#!/usr/bin/env python
import cyt

if __name__ == "__main__":
    import random
    rs = [2 + 2 * random.random() for i in range(500)]
    xs = [random.random() for i in range(200)]
    import svg
    import time
    started = time.time()
    with open("test.svg", "w") as fout:
        for line in svg.draw(cyt.everything(sorted(rs), sorted(xs), 2000)):
            print >> fout, line
    print "steps/s", 500 * 200 * 2000 / (time.time() - started)
