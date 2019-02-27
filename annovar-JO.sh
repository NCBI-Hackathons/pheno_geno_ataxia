#!/bin/bash

# written by Segun Fatumo (and then hacked up a lot by Jenna Oberstaller to get around our sub-optimal permissions situation on our vm; this will be much less complicated on a single-owner environment)

#script assumes that databses have previously been downloaded

#run TABLE_ANNOVAR, using ExAC version 0.3 (referred to as exac03) dbNFSP version 3.0a (referred to as dbnsfp30a), dbSNP version 147 with left-normalization (referred to as avsnp147) databases and remove all temporary files, and generates the output file called myanno.h

# JO: changed loop to act on all .vcf files in the Related_Individuals directory and to output to a shared directory (necessitates the loop changing directories a couple times; sudo to get around the various permissions)

#format vcf file to avinput
cd /home/Data/1000_Genomes_Phase3/Related_Individuals/

for f in *.vcf;do
sudo cat $f | fgrep -v "##" | awk 'BEGIN{OFS="\t"}NR>1{print $1,$2,$2,$4,$5,"comments: "$3}' > /home/Annovar_Output/$f.avinput

cd /home/Annovar_Output

sudo table_annovar.pl $f.avinput humandb/ -buildver hg19 -out $f -remove -protocol refGene,cytoBand,exac03,avsnp147,dbnsfp30a -operation gx,r,f,f,f -nastring . -csvout -polish -xref /usr/local/bin/annovar/example/gene_xref.txt

#format result
awk -F "," 'BEGIN{OFS="\t"}{print $1,$2,$3,$4,$5,$6,$7,$8,$21,$24, $25, $26, $27}' $f.hg19_multianno.csv > /home/Annovar_Output/formatted_$f.txt

cd /home/Data/1000_Genomes_Phase3/Related_Individuals/

done