#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    segments = line.split()
    time = segments[3][1:15]
    print('%s\t%s' % (time, 1))
