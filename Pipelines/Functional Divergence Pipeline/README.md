# Functional DIvergence Pipeline

The GroupSim pipeline is used for identifying and filtering functional divergent (FD) sites in multiple sequence alignments (MSA).
The pipeline takes as input a MSA, two grouping files with the names of the species in the two groups, and the percentage of most divergent sites to filter out. 


GroupSim is used to score FD sites. It is written by Tony Capra (2008).

Reference: Capra JA and Singh M. (2008) Characterization and Prediction of
Residues Determining Protein Functional Specificity. Bioinformatics,
24(13): 1473-1480, 2008.

## Usage:

./gspipe -i {input} -p {output prefix}  -n {percentage} -f {first group} -s {second group}

for seperating the most (m) and least (l) divergent sites according to user specified percentages.

All options must be specified.

Options | Details 
--------|--------
 input  | The original sequence alignment in phylip format
 output prefix | The string to prefix to output files
 percentage | The % of sites to filter (see output section)
 first group | Filename of the 1st group of organisms, one species per line
 second group | Filename of the 2nd group of organisms, one species per line

#### Output
The two key output files are `{output_prefix}_lnfd.txt` and `{output_prefix}_mnfd.txt`. They contain the filtered alignments according to functional divergence scores. **L** and **M** stands for the least and most divergent sites respectively. 

If the input for {percentage} is 40, then 40% of the sites will end up in `{output_prefix}_lnfd.txt`, and 60% in `{output_prefix}_mnfd.txt`. 

## Requirement:
1. R - version 4.x
2. Python - version 3.x

## Python Packages Needed:
Pandas, numpy, BioPython

## R packages Needed:
vroom, stringr, tidyverse
