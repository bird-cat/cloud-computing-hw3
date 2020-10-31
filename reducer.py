#!/usr/bin/env python

from operator import itemgetter
import sys

current_t = None
current_count = 0
t = None

for line in sys.stdin:
    line = line.strip()
    t, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_t == t:
        current_count += count
    else:
        if current_t:
            # write result to STDOUT
            print('%s\t%s' % (current_t, current_count))
        current_count = count
        current_t = t

if current_t == t:
    print('%s\t%s' % (current_t, current_count))
