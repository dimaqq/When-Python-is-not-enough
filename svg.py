#!/usr/bin/env python
def draw(data):
    yield """<svg xmlns="http://www.w3.org/2000/svg"
              version="1.2" width="1020" height="520">
              <g transform="translate(-990, 510) scale(500, -500)">
               <rect x="2" width="2" height="1"
                fill="none" stroke="black"
                stroke-width=".001"/>"""

    last = object()
    for point in data:
        if point == last:
            continue
        yield """<circle cx="%s" cy="%s"
                  r=".002" fill="black"/>""" % point
        last = point

    yield """ </g>
             </svg>"""
