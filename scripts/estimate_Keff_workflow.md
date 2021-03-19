# Estimating per-site K_effs

1. Run an analysis using PhyloBayes CAT-Poisson (can be with a fixed topology), or using IQ-TREE and the PMSF model (-m LG+C60+F+G -ft guidetree). 
2. Create a site profiles file (readpb_mpi -ss, or use the .sitefreq from IQ-TREE). Use one of the two scripts to covert site frequencies to site Keffs (site-dists: IQ-TREE .sitefreq; siteprofiles: the PhyloBayes output).
3. The .keffs file contains per-site Keffs.
