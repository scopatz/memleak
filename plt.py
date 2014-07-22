#! /usr/bin/env python 
import sys
import io

from matplotlib import pyplot as plt

def readf(fname):
    with io.open(fname) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]
    n = [int(x.split()[0]) for x in lines if len(x) > 0]
    mem = [float(x.split()[1]) / 1e3 for x in lines if len(x) > 0] # kb to mb
    return n, mem

def main():
    fnames = sys.argv[1:]
    plt.rc('lines', linewidth=2)
    plt.rc('axes', color_cycle=['r', 'g', 'b', 'y'])

    fig, ax = plt.subplots()
    for fname in fnames:
        n, mem = readf(fname)
        ax.plot(n, mem)
    ax.set_xlabel('divisions')
    ax.set_ylabel('memory (mb)')
    ax.legend(fnames)
    plt.savefig('fig.png')

if __name__ == '__main__':
    main()

