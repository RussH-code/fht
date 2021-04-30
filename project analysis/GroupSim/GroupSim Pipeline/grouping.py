#!/usr/bin/python3

import glob, os, sys, getopt

inputfile = ''
prefix = ''
group1 = ''
group2 = ''

try:
    opts, args = getopt.getopt(sys.argv[1:],"i:p:f:s:")
except getopt.GetoptError:
    print ('test.py -i <inputfile> -p <outputfile>')
    sys.exit(2)
   
for opt, arg in opts:
    if opt in ("-i"):
        inputfile = arg
    elif opt in ("-p"):
        prefix = arg
    elif opt in ("-f"):
        group1 = arg
    elif opt in ("-s"):
        group2 = arg

with open(group1, "r") as f:
    line1 = f.readlines()
with open(group2, "r") as f:
    line2 = f.readlines()
   
list1 = [i.strip() for i in line1]
list2 = [i.strip() for i in line2]

for filepath in glob.iglob(inputfile):
    output = prefix + "_groupsim.fas"
    with open(filepath, "r") as f:
        lines = f.readlines()
    original_stdout = sys.stdout
    print("Writing to ", output)
    with open(output, "w") as g:
        sys.stdout = g
        print(lines[0].strip())
        for line in lines[1:]:
            a = line.split()
            white_space_length = 30 - len(a[0])
            if a[0] in list1:
                group = "|euk"
            elif a[0] in list2:
                group = "|bac"
            else:
                print("Error")
            group = group + " " * white_space_length
            a.insert(1, group)

            print("".join(a))
        sys.stdout = original_stdout
