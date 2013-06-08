#!/usr/bin/env python
import ctypes
ctm = ctypes.CDLL("./libctm.so")
ctm.stepx.restype = ctypes.c_float
ctm.stepx.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_int]


def everything(rs, xs, count):
    for r in rs:
        for x in xs:
            x = ctm.stepx(r, x, count)
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
