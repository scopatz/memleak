#! /usr/bin/env python
from __future__ import print_function
import sys
import glob
import gc
import resource

N = 10**4
freq = N/100

buildlib = glob.glob('build/lib.*')
sys.path.insert(0, buildlib[0])

from memleak.hollow import Hollow

for n in xrange(N):
    #gc.collect()
    h = Hollow()
    del h
    if n%freq == 0:
        print(n/freq, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        sys.stdout.flush()

print()
