# Find FD sites on a target branch of the tree

1. Split the alignment into taxa on either side of the target branch with write_split_alignments.py. Two text files with the list of taxa to be in each subalignment can be provided as input.
2. For each half of the alignment, obtain site-specific frequencies via PhyloBayes or IQ-TREE PMSF: (i) Estimate a guide tree (e.g. IQ-TREE); (ii) run pb chain with fixed topology (-T); (iii) use readpb_mpi -ss to obtain .siteprofiles file for each half of the alignment.
3. Calculate site profile distance for each site using calc_profile_dist.py. This script reports the Euclidean distance between each pair of site profiles on either side of the alignment. Higher dist corresponds, perhaps, with greater FD.
