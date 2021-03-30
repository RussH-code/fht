# Site Rate Shift

1. Use write_split_alignments.py in scripts to split the alignment of interest into two
2. Generate seperate trees for each half of the alignment and infer the rate with iqtree `--rate`
3. Use site_rate_shift.py to compare rate shifts across the sites 

Usage: python site_rate_shift.py -a *1st rate file* -b *2nd rate file* -o *output file name*