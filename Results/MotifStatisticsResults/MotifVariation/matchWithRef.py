import os
import sys

# Input
inFile = open(sys.argv[1],"r")
outFile = open(sys.argv[2],"w")

# Reading reference
refList = []
invDict = dict([("A","T"),("T","A"),("C","G"),("G","C")])
refFile = open("/work/eg474423/eg474423_Projects/trunk/Myc/MotifStatistics/MotifVariation/ref.txt","r")
for line in refFile:
    ll = line.strip()
    refList.append(ll)
    refList.append("".join([invDict[e] for e in ll[::-1]]))
refFile.close()

# Matching
countDict = dict()
for line in inFile:
    ll = line.strip()
    if(ll not in refList): outFile.write("ERROR: "+ll+"\n")
    try: countDict[ll] += 1
    except Exception: countDict[ll] = 1
inFile.close()

# Writing
for k in countDict.keys(): outFile.write(k+"\t"+str(countDict[k])+"\n")
outFile.close()

# ['CACGCG', 'CGCGTG', 'CACGTG', 'CACGTG', 'CATGCG', 'CGCATG', 'CACGAG', 'CTCGTG', 'CATGTG', 'CACATG', 'CAACGTG', 'CACGTTG']
