import getopt, re, sys
import numpy as np
import pandas as pd

ghost_tree = ""
site_prob = ""
output = ""

try:
    opts, args = getopt.getopt(sys.argv[1:],"g:s:o:")
except getopt.GetoptError:
    print ('-g <ghost treefile> -s <site probability file> -o <output>')
    sys.exit(2)
    
for opt, arg in opts:
    if opt in ("-g"):
        ghost_tree = arg
    elif opt in ("-s"):
        site_prob = arg
    elif opt in ("-o"):
        output = arg

with open(ghost_tree, "r") as f:
    trees = f.readlines()
    
n = len(trees) - 1  ## Number of partitions
trees = trees[0]

ind_tree = re.findall("(?:\d+\.?\d*\/)+\d+\.?\d*", trees)  ## Get a list of all branch lenghts of individual trees
con_tree = re.findall("(?<=\:)\d+\.?\d*", trees)             ## Get a list of branch lengths of the consensus tree

ind_bl = [list(map(float, i.split('/'))) for i in ind_tree]  ## Convert to float for calculations and remove delimiter
con_bl = list(map(float, con_tree))

## Calculater heterotachy score per partition using euclidean distance
partition_score = np.linalg.norm(np.array(ind_bl).T - con_bl, ord = 2, axis = 1)

sp = pd.read_csv(site_prob, delimiter = '\t')
sp = sp.iloc[:, 1:n+1].multiply(partition_score, axis = 1)
sp['total'] = sp.sum(axis = 1)
sp['site'] = sp.index +1

sp.to_csv(output, sep = '\t')
print("Output has been written to ", output)