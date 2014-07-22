#! /usr/bin/env python
from __future__ import print_function
import sys
import glob
import gc

N = 10**7
Ndiv10 = N/10

buildlib = glob.glob('build/lib.*')
sys.path.insert(0, buildlib[0])

from memleak.hollow import Hollow

for n in xrange(N):
    #gc.collect()
    h = Hollow()
    del h
    if n%Ndiv10 == 0:
        print(n/Ndiv10, end=" ")
        sys.stdout.flush()

print()