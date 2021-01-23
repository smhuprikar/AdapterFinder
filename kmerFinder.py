#!/usr/bin/env python3
# Adapter/Kmer Finder script outputs list of kmers and sort them acc frequency from seq data
# Swati Mishra swatim@outlook.com
# 04/03/2019
import sys

#parsing arguments
# Usage :python kmerFinder.py fastqFile kmer eq: python kmerFinder.py samplefastq.fq 4 
# AdapterFinderResults.txt CONTAINS Kmer Results and Frequency this is created in the same 

#parsing argument file and kmer length
if len(sys.argv) == 3:
    fqFile = sys.argv[1]
    k = int(sys.argv[2])
else:    
    fqFile = r"/Users/swatimishra/samplefastq.fq"
    k = 6
verbose=True
sys.stdout = open('AdapterFinderResults.txt','wt')
#reading the file    
with open(fqFile) as f:
    fqLines = f.read()
lines = [line.strip() for line in fqLines.split('\n') if line != '']
#print(lines)

countFromKmer = {}
#looping through the file
for line in lines[1::4]:
    idxFirst= 0
    #print(len(line))
    while idxFirst + k <= len(line):
        kmer = line[idxFirst:(idxFirst+k)] #extracting those kmers
        countFromKmer[kmer] = countFromKmer.get(kmer, 0) + 1 #Kmer counts
        idxFirst += 1
 
#values and sorting the kmers            
kmerCounts = list(countFromKmer.items())
kmerCounts.sort(reverse = True, key = lambda kmerCount: kmerCount[1])
#print(kmerCounts)

if verbose:
    totalNoKmers = sum(countFromKmer.values())
    print("----------Results-------------")
    print("Total Number of Kmers: %d" % totalNoKmers)
    #print(list(countFromKmer.keys()))
print("----Kmer list and Frequency----")
for kv in kmerCounts:
    print ('%s %d' % kv) #Kmers list and frequency

print("-------------------------------")
