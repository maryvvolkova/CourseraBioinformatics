from random import choice
import numpy as np

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
        print(Neighborhood)
        return Neighborhood

def Reverse_Complement(DNA):
    DNA_seq = Seq(DNA)
    DNArc_seq = DNA_seq.reverse_complement()
    DNArc = str(DNArc_seq)
    return DNArc

def IterativeNeighbors(Pattern, d):
    print('Entered Iterative Neighbors with Pattern ' + Pattern + ' and d ' + str(d))
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


def MotifEnumeration(DNA, k, d):
    Patterns = []
    print(len(DNA))
    DNA_1 = DNA[0]
    for i in range(len(DNA_1)-k+1):
        Pattern = DNA_1[i:i+k]
        print('Current pattern is: ' + Pattern)
        Neighborhood = IterativeNeighbors(Pattern, d)
        for neighbor in Neighborhood:
            Patterns.append(neighbor)
        print(Neighborhood)
        for DNA_i in DNA:
            for Neighbor in Neighborhood:
                if Neighbor in DNA_i:
                    i += 1
                    print('Neighbor ' + Neighbor + ' is in ' + DNA_i)
            if len(DNA) <= i:
                Patterns.append(Neighbor)
    Patterns = list(set(Patterns))
    return Patterns


'''bases = ['A','T','G','C']
DNA = ''
k = 10
for i in range(k):
    base = choice(bases)
    DNA += base
print(DNA)
'''

with open('dataset_156_8.txt', 'r') as file:
    lines = file.readlines()
    nums = lines[0].rstrip()
    k = int(nums.split(' ')[0])
    print(k)
    d = int(nums.split(' ')[1])
    print(d)
    DNAs = lines[1].rstrip()
    print(DNAs)
    DNA_arr = DNAs.split(' ')
    print(DNA_arr)

Patterns = MotifEnumeration(DNA_arr, k, d)
print(*Patterns)
