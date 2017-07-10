#!/bin/zsh

# Parameters
fastaFile="/hpcwork/izkf/projects/egg/Data/HG19/hg19.fa"
il="/work/eg474423/eg474423_Projects/trunk/Myc/MotifStatistics/MotifVariation/250/"
inFolderList=( $il"Nhek_cMyc_summits/" $il"Nhek_cmyc_wdr5/" $il"Nhek_wdr5_summits/" )

# Folder Loop
for inFolder in $inFolderList
do

    # Check if perfect motif matching
    fastaFromBed -tab -fi $fastaFile -bed $inFolder"mpbs.bed" -fo $inFolder"temp.fa"
    python upcase.py $inFolder"temp.fa" $inFolder"temp2.fa"
    cut -f2 $inFolder"temp2.fa" | sort | uniq > $inFolder"temp3.fa"
    python matchWithRef.py $inFolder"temp3.fa" $inFolder"valid1.txt"
    rm $inFolder"temp.fa" $inFolder"temp2.fa" $inFolder"temp3.fa"

    # Check random overlap with CATGTG
    grep catgtg $inFolder"mpbs.bed" > $inFolder"temp1.txt"
    grep cacatg $inFolder"mpbs.bed" > $inFolder"temp2.txt"
    cat $inFolder"temp1.txt" $inFolder"temp2.txt" > $inFolder"temp3.bed"
    intersectBed -a $inFolder"rand.bed" -b $inFolder"temp3.bed" | sort > $inFolder"apagar1.txt"
    intersectBed -a $inFolder"rand.bed" -b $inFolder"temp3.bed" | sort | uniq > $inFolder"apagar2.txt"
    intersectBed -a $inFolder"rand.bed" -b $inFolder"temp3.bed" | sort | uniq | wc -l > $inFolder"temp4.txt"
    intersectBed -v -a $inFolder"rand.bed" -b $inFolder"temp3.bed" | sort | uniq | wc -l > $inFolder"temp5.txt"
    cat $inFolder"temp4.txt" $inFolder"temp5.txt" > $inFolder"valid2.txt"
    rm $inFolder"temp1.txt" $inFolder"temp2.txt" $inFolder"temp3.bed" $inFolder"temp4.txt" $inFolder"temp5.txt"

done



