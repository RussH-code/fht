from __future__ import print_function
from Bio import SeqIO
import re, sys

sites_to_print = [] #so these are the ones which we want to KEEP
#keffs
inh = open("rnapol_keffs.txt")
for line in inh:
	fields = re.split(",", line.rstrip())
	site = int(fields[0])
	if float(fields[1]) < 10:
		sites_to_print.append(site)
inh.close()

seqs = SeqIO.index(sys.argv[1], "fasta")
for seq in seqs:
	inseq = str(seqs[seq].seq)
	outseq = ''
	print(">" + seqs[seq].description)
	for site in sites_to_print:
		character = site - 1
		outseq = outseq + inseq[character]
	print(outseq)

