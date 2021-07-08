#!/bin/bash/python3

import glob, getopt, os, sys, math
import numpy as np
import pandas as pd
from Bio import SeqIO

sitesfile = ""
inputfile = ""
prefix = ""

try:
    opts, args = getopt.getopt(sys.argv[1:],"i:s:p:")
except getopt.GetoptError:
    print ('-i <inputfile> -s <sites file>')
    sys.exit(2)
    
for opt, arg in opts:
    if opt in ("-i"):
        inputfile = arg
    elif opt in ("-s"):
        sitesfile = arg
    elif opt in ("-p"):
        prefix = arg

for filepath in glob.iglob(inputfile):
    output = prefix + ".phy"
    
    with open(sitesfile, "r") as f:
        lines = f.readlines()

    nfd_sites = sorted([int(i) + 1 for i in lines[0].split()])

    with open(inputfile, "r") as d:
        lines = d.readlines()

    species = []
    protein = []

    for line in lines[1:]:
        species.append(line.split()[0])
        protein.append(line.split()[1])
    msa = pd.DataFrame(protein)[0].str.split("", expand=True)
    msa = msa[nfd_sites]    
    out = pd.DataFrame({"species": species, "protein":msa.values.sum(axis = 1)})
    with open("temp.fas", 'w') as f:
        for i in range(out.shape[0]):
            taxa = ">" + out["species"][i]
            f.write(taxa + "\n")
            data = out["protein"][i]
            chunks = [data[x:x+60] for x in range(0, len(data), 60)]
            for j in range(len(chunks)):            
                f.write(chunks[j] + "\n")
    record = SeqIO.parse("temp.fas", "fasta")
    SeqIO.write(record, output, "phylip-relaxed")

print("Finished! Results have been written to ", output)
