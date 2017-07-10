import os
import sys
inFile = open(sys.argv[1],"r")
outFile = open(sys.argv[2],"w")
for line in inFile:
    ll = line.strip().split("\t")
    outFile.write("\t".join([ll[0],ll[1].upper()])+"\n")
inFile.close()
outFile.close()
