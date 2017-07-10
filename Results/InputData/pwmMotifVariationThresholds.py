
# Import
import os
import sys
import glob
from Bio import Motif

# Input
inFolder = "/work/eg474423/eg474423_Projects/trunk/Myc/InputData/PWM_MotifVariation/"
fprV = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001]

# Execution
outFile = open("pwmMotifVariationThresholds.txt","w")
for inFileName in glob.glob(inFolder+"*.pwm"):
    pwmFile = open(inFileName,"r")
    pwm = Motif.read(pwmFile,"jaspar-pfm")
    pwmFile.close()
    maxS = pwm.max_score()
    sd = Motif.ScoreDistribution(pwm,precision=10**4)
    scoreV = [sd.threshold_fpr(e) for e in fprV]
    outFile.write(inFileName.split("/")[-1].split(".")[0]+"\n")
    outFile.write("Max = "+str(maxS)+"\n")
    outFile.write("\n".join(["\t".join([str(fprV[i]),str(scoreV[i])]) for i in range(0,len(fprV))])+"\n\n")
outFile.close()


