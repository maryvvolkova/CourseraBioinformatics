from Bio.Seq import Seq
import numpy as np
import matplotlib.pyplot as plt
import re


def ImmediateNeighbors(Pattern, d):
        if d == 0:
            return {Pattern}
        if len(Pattern) == 1:
            return list({'A', 'C', 'G', 'T'})
        Neighborhood = set()
        Neighborhood.add(Pattern)
        for i in range(len(Pattern)): #3 = will do 4 times
            symbol = Pattern[i]
            for x in 'ATGC':
                if x != symbol:
                    Neighbor = Pattern[:i] + x + Pattern[i+1:]
                    Neighborhood.add(Neighbor)
        Neighborhood=list(Neighborhood)
        return Neighborhood

def Reverse_Complement(DNA):
    DNA_seq = Seq(DNA)
    DNArc_seq = DNA_seq.reverse_complement()
    DNArc = str(DNArc_seq)
    return DNArc

def IterativeNeighbors(Pattern, d):
    neighborhood=[Pattern]
    for j in range(d): #will do 3 times if d = 2
        for string in neighborhood:
            neighbors_list = ImmediateNeighbors(string, j)
            if len(neighbors_list) > 1:
                for neighbor in neighbors_list:
                    neighborhood.append(neighbor)
            neighborhood=list(set(neighborhood)) #duplicate removal
    return neighborhood


def MaxMap(freqMap):
    values = freqMap.values()
    return max(values)

def FrequentWordsWithMismatches(DNA, k, d):
    Patterns = []
    freqMap = {}
    n = len(DNA)
    for i in range(n - k + 1):
        Pattern = DNA[i:i+k]
        Pattern_rc = Reverse_Complement(Pattern)
        neighborhood_st = IterativeNeighbors(Pattern, d)
        neighborhood_rc = IterativeNeighbors(Pattern_rc, d)
        neighborhood = neighborhood_st + neighborhood_rc
        for neighbor in neighborhood:
            freqMap[neighbor] = freqMap.get(neighbor, 0) + 1


    m = MaxMap(freqMap)
    for Pattern in freqMap:
        if freqMap[Pattern] == m:
            Patterns.append(Pattern)

    return Patterns


def readFasta (f: str):
    """
    Reads a fasta file and
    Returns a dictionary with ID as key and sequence as value.
    """
    fastaFile = open(f, 'r')
    fastaLines = fastaFile.readlines()
    seqID = "" 
    seq = ""
    fastaSeqs = {}
    for line in fastaLines:
        if line.startswith('>'):
            fastaSeqs[seqID] = seq
            seqID = line.rstrip().removeprefix('>')
            seq = ""
        else:
            seq += line.rstrip()
    fastaSeqs[seqID] = seq
    fastaSeqs.pop('')
    fastaFile.close()

    return fastaSeqs


DNA = list(readFasta('Salmonella_enterica.txt').values())[0]
DNA_window = DNA[3764355:3765355]

answer = FrequentWordsWithMismatches(DNA_window, 9, 1)
answer = list(set(answer))
print(answer)