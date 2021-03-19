#!/usr/bin/env python3

import argparse
import os
import numpy as np
import pandas as pd

d = """Convert PMSF site distributions to effective number of amino acids.
"""


def parse_arguments():
    parser = argparse.ArgumentParser(description=d)
    parser.add_argument('infile', help="IQ-TREE site distribution file.")
    return parser.parse_args()


a = parse_arguments()
fn = a.infile
of = os.path.splitext(fn)[0] + ".keff"


def np_array_to_string(a, d=' '):
    """Convert a numpy array to a string."""
    x_arrstr = np.char.mod('%.8f', a)
    return d.join(x_arrstr)


def p_homo(a):
    """Homoplasy."""
    # return sum([x**2 for x in a])
    return np.sum(np.square(a))


def keff_homoplasy(a):
    """Effective number of amino acids (homoplasy)."""
    return 1.0/np.sum(np.square((a)))


df = pd.read_table(fn, sep=r'\s+', header=None, index_col=0)
df.index.names = ['Site']
df = df.apply(func=keff_homoplasy, axis=1)
df.to_csv(of)
