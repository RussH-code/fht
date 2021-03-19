#for each site, calculate (Euclidean) distance between site profiles in two halves of the alignment (across target branch)

import os, sys, re
from collections import defaultdict
import numpy as np

def isInt(string): #lol
	try:
		int(string)
		return True
	except ValueError:
		return False

def read_siteprofile_file(sp_file):
	profile = defaultdict(list)
	inh = open(sp_file)
	for line in inh:
		fields = re.split("\t", line.rstrip())		
		if isInt(fields[0]):
			profile[fields[0]] = np.array(list(map(float, fields[1:])))
	return profile		

sp1_file = sys.argv[1]
sp2_file = sys.argv[2]

sp1 = read_siteprofile_file(sp1_file)
sp2 = read_siteprofile_file(sp2_file)

results = {}
for site in sp1.keys():
	dist = np.linalg.norm(sp1[site] - sp2[site])
	results[int(site)] = dist
sorted_results = sorted(results.keys())
print("Site\tProfileDist")
for site in sorted_results:
	print(str(site) + "\t" + str(results[site]))
