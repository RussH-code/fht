# Compositional Shift

The Compositional Shift pipeline is used for identifying and filtering sites that have experienced compositional changes during evolution.
The pipeline takes as input a MSA, two site frequency files with the amino acid distributions in two groups of organisms, and the percentage of sites to filter out. 

## Usage:

./cspipe -f {first site freq} -s {second site freq} -o {freq output} -p {percentage} -a {alignment} -u {finalouput}

All options must be specified.

## Input:
The site frequency files can be prepared by running iqtree on two groups of organisms on the same sites with `PMSF` model to infer the site-specific frequencies. For details, take a look at Section **Site-specific frequency models** on http://www.iqtree.org/doc/Complex-Models

Options | Details 
--------|--------
 first site freq  | Site-specific frequency for first group of organisms
 secondrate | Site-specific frequency for second group of organisms
 freq output | The name of the frequency comparison file in output
 percentage | The percentage of sites to filter
 alignment | The original multiple sequence alignment in phylip format
 finaloutput | The filename for the finaloutput alignment file

#### Output
The two key output files are `{finaloutput}_cs_top{percentage}.phy` and `{finaloutput}_cs_bottom{percentage}.phy`, which contains the sites that have experienced the most and least amount of compositional shifts. 

If the input for {percentage} is 40, then 40% of the sites will end up in `{finaloutput}_rs_bottom{percentage}.phy`, and 60% in `{finaloutput}_rs_top{percentage}.phy`. 

## Requirement:
1. R - version 4.x
2. Python - version 3.x

## Python Packages Needed:
Pandas, numpy, BioPython

## R packages Needed:
vroom, stringr, tidyverse
