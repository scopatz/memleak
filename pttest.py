#! /usr/bin/env python 
from __future__ import print_function
import os
import gc
import sys

import numpy as np
import tables as tb

N = 10**5
Ndiv10 = N/10

_N_CAPS_MAX = 10

exarc = np.dtype([
    ("instid", ('str', 16)), # 16 bytes for uuid
    ("id", np.int64),
    ("uid", np.int64),
    ("ucaps", (np.float64, _N_CAPS_MAX),), # array of size N_CAPS_MAX
    ("vid", np.int64),
    ("vcaps", (np.float64, _N_CAPS_MAX),), # array of size N_CAPS_MAX
    ("pref", np.float64),
    ])

data = np.empty(N, dtype=exarc)

with tb.open_file('x.h5', 'w') as f:
    tab = f.create_table('/', 'tab', exarc, chunkshape=(N/1000,))
    row = tab.row
    for n, dat in enumerate(data):
        gc.collect()
        for name in exarc.names:
            row[name] = dat[name]
        row.append()
        tab.flush()
        if n%Ndiv10 == 0:
            print(n/Ndiv10, end=" ")
            sys.stdout.flush()
print()