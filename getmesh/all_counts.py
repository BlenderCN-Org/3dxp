import glob
import os, h5py
import numpy as np
import sys, argparse
from threed import ThreeD
from scripts import biggest
from scripts import deepest

def start(_argv):

    args = parseArgv(_argv)
    # expand all system paths
    homepath = lambda pathy: os.path.expanduser(pathy)
    realpath = lambda pathy: os.path.realpath(homepath(pathy))
    sharepath = lambda share,pathy: os.path.join(share, homepath(pathy))

    BLOCK = args['block']
    ROOTOUT = realpath(args['out'])
    DATA = realpath(args['ids'])
    # Count most spread or deep ids 
    biggest(DATA, sharepath(ROOTOUT,'spread_count.txt'), BLOCK)
    deepest(DATA, sharepath(ROOTOUT,'deep_count.txt'), BLOCK)

def parseArgv(argv):
    sys.argv = argv

    help = {
        'ids': 'input hd5 id volume (default in.h5)',
        'out': 'output text list directory (default .)',
        'b': 'Number of blocks in each dimension (default 10)',
        'help': 'Save the deepest and biggest cells'
    }

    parser = argparse.ArgumentParser(description=help['help'])
    parser.add_argument('-b','--block', type=int, default=10, help=help['b'])
    parser.add_argument('ids', help=help['ids'])
    parser.add_argument('out', help=help['out'])

    # attain all arguments
    return vars(parser.parse_args())

def main(*_args, **_flags):
    return start(toArgv(*_args, **_flags))

if __name__ == "__main__":
    print start(sys.argv)
