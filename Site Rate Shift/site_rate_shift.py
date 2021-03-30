import pandas as pd
import numpy as np
import getopt, sys

rate_file_a = ""
rate_file_b = ""
output = ""

try:
    opts, args = getopt.getopt(sys.argv[1:],"a:b:o:")
except getopt.GetoptError:
    print ('-a <1st rate file> -b <2nd rate file> -o <output>')
    sys.exit(2)
    
for opt, arg in opts:
    if opt in ("-a"):
        rate_file_a = arg
    elif opt in ("-b"):
        rate_file_b = arg
    elif opt in ("-o"):
        output = arg

rate_a = pd.read_csv(rate_file_a, skiprows=8, delimiter='\t').sort_values(by="Rate", ignore_index=True)
rate_b = pd.read_csv(rate_file_b, skiprows=8, delimiter='\t').sort_values(by="Rate", ignore_index=True)

rate_a['Rank_a'] = rate_a.index + 1
rate_b['Rank_b'] = rate_b.index + 1
rate_a.drop(["Rate", "Cat", "C_Rate"], axis=1, inplace=True)
rate_b.drop(["Rate", "Cat", "C_Rate"], axis=1, inplace=True)

merged = pd.merge(rate_a, rate_b, how='left', on=['Site'])
merged["score"] = abs((merged['Rank_a'] - merged['Rank_b']))/len(merged)*100
merged.sort_values(by='Site', ignore_index=True)

merged.to_csv(output, sep = '\t', index=False)
print("Output has been written to ", output)