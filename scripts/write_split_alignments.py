#read an alignment with two sets of taxa (either side of key split) and write two alignments, one for each side

from Bio import SeqIO
import sys

alignment = SeqIO.index(sys.argv[1], "fasta")

def subalignment(aln_dict, taxa_file):
	target = []
	subaln = {}
	inh = open(taxa_file)
	for line in inh:
		target.append(line.rstrip())
	inh.close()
	for rec in aln_dict:
		if aln_dict[rec].id in target:
			subaln[aln_dict[rec].id] = str(aln_dict[rec].seq)
	return subaln

def write_alignment(aln_dict, outname):
	outh = open(outname, "w")
	for seq in aln_dict:
		outh.write(">" + seq + "\n" + aln_dict[seq] + "\n")
	outh.close()
	return
		

#read in the two taxa sets

subA = subalignment(alignment, sys.argv[2])
subB = subalignment(alignment, sys.argv[3])

write_alignment(subA, sys.argv[2] + "_subA")
write_alignment(subB, sys.argv[3] + "_subB")

#for seq in subA:
#	print(seq + "\n" + subA[seq] + "\n")

