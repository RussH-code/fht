# Site Rate Shift 

The Site Rate Shift pipeline is used for identifying and filtering sites that have experienced changes in evolutionary rates.
The pipeline takes as input a MSA, two rate files with the evolutionary rates of sites in two groups of organisms, and the percentage of sites to filter out. 

## Usage:

./srpipe -f {firstrate} -s {secondrate} -o {rateoutput} -p {percentage} -a {alignment} -u {finalouput}

All options must be specified.

## Input:
The rate files can be prepared by running iqtree on two groups of organisms on the same sites with `--rate` options to infer the site-specific rates. For details, take a look at Section **Inferring Site-Specific Rate** on http://www.iqtree.org/doc/Advanced-Tutorial 

Options | Details 
--------|--------
 input  | The original sequence alignment 
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
