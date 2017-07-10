
# Import
import os
import sys
import glob

# Input
sizes = [80,100,250,500]
inputList = glob.glob("./All_Epigeneticcode/*.bed")

# Execution
for inputFileName in inputList:
    inputFile = open(inputFileName,"r")
    outFileList = [open("./Epigeneticcode/"+str(e)+"/"+inputFileName.split("/")[-1],"w") for e in sizes]
    for line in inputFile:
        ll = line.strip().split("\t")
        p1 = int(ll[1]); p2 = int(ll[2]); mid = (p2+p1)/2
        for i in range(0,len(sizes)): outFileList[i].write("\t".join([ll[0],str(mid-(sizes[i]/2)),str(mid+(sizes[i]/2))]+ll[3:])+"\n")
    inputFile.close()
    for e in outFileList: e.close()


