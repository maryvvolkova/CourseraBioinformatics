import string
import itertools

def generate_strings(k):
    for item in itertools.product('ATGC', repeat=k):
        yield "".join(item)

def existing_strings(k, dna):
    existing_patterns = []
    l = len(dna[0])
    for idna in dna:
        for i in range(l - k + 1):
            existing_patterns.append(idna[i:i+k])
    print(existing_patterns)
    return existing_patterns

    

def HammingDistance(seq1, seq2):
    return len([i for i in range(len(seq1)) if seq1[i] != seq2[i]])

def PatternStringDistance(pattern, dna):
    k = len(pattern)
    distance = 0
    for seq in dna:
        print(seq)
        l = len(seq)
        hd = float('inf')
        for i in range(l - k + 1):
            hdCurr = HammingDistance(pattern, seq[i:i+k])
            if hd > hdCurr:
                hd = hdCurr
        distance += hd
    print(distance)
    return distance


def MedianString(k, dna):
    d = {}
    for item in existing_strings(k, dna):
        d[item] = (PatternStringDistance(item, dna))
    return min(d, key=d.get)
    
    
with open('dataset_158_9.txt', 'r') as file:
    lines = file.readlines()
k = int(lines[0].rstrip())
dna = [lines[i].rstrip() for i in range(len(lines)) if i >= 1]
print(dna)

print (MedianString(k, dna))
