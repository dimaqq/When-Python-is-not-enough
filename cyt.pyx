cimport cython


def everything(rs, xs, count):
    cdef int i
    cdef float r
    cdef float x
    for r in rs:
        for x in xs:
            with nogil:
                for i in range(count):
                    x = r * x * (1 - x)
            yield (r, x)
