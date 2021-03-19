#Find FD sites on a target branch of the tree

1. Split the alignment into taxa on either side of the target branch with write_split_alignments.py.
2. For each half of the alignment, obtain site-specific frequencies via PhyloBayes or IQ-TREE PMSF.
3. Calculate site profile distance for each site using calc_profile_dist.py
