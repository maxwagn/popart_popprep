# !/usr/bin/env python
# written by Maximilian Wagner

# USAGE: python popart_popprep_v1.py <inputfile.nex> <outputfile.nex> <metadata.csv>

import sys

input = {}
list = []
indexer = []
popcode = []
out = str()

NEXUS_inputfile = sys.argv[1]
NEXUS_outputfile = sys.argv[2]
CSV_metadata = sys.argv[3]

with open(CSV_metadata) as fh:
    for line in fh:
        line = line.rstrip()
        input[line.split(',')[0]] = line.split(',')[1]
    for k, v in input.items():
        if v in list:
            pass
        else:
            list.append(v)

for i in list:
    indexer.append(list.index(i))

trait_labels = str()

for i in list:
    str(list).strip('[]')
    str(list).strip(',')
    str(list).strip('''''')
    trait_labels += i + " "

for j in indexer: ### writes population code 1,0,0,0....
    popcode.append(('0,'* j + '1,' + "0," * ((len(indexer) - 1) - j))[:-1])

meta = dict(zip(list, popcode))

out += "Begin Traits;\n" \
       "\tDimensions NTRAITS="+str(len(list))+";\n\tFormat labels=yes missing=? separator=Comma;\n" \
       "\tTraitLabels " + trait_labels[:-1] + ";\nMatrix\n\n"


for k,v in input.items():
    for key,val in meta.items():
        if v == key:
            out += k + " " + val +"\n"

out += ";\nEND;"

with open(NEXUS_inputfile, 'r') as f1, open(NEXUS_outputfile, 'w') as f2:
    f2.write(f1.read() + "\n\n" + out)

