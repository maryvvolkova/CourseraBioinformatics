'''def HammingDistance(DNA1, DNA2):
    HD = 0
    for n in range(len(DNA1)):
        print(DNA1)
        print(DNA2)
        if DNA1[n] != DNA2[n]:
            HD += 1
    return HD
'''

def HammingDistance(DNA1, DNA2):
    return len([i for i in range(len(DNA1)) if DNA1[i] != DNA2[i]])

def DistanceBetweenPatternAndStrings(Pattern, Dna):
    k = len(Pattern)
    distance = 0
    for Text in Dna:
        n = len(Text)
        HD = float('inf') 
        for i in range(n - k + 1):
            Pattern_1 = Text[i:i+k]
            if HD > HammingDistance(Pattern, Pattern_1):
                HD = HammingDistance(Pattern, Pattern_1)
        distance += HD
    return distance

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

def AllStrings(k):
    a = []
    DNA = ''
    for i in range(k):
        DNA += 'A'
    for i in range(k):
        a += IterativeNeighbors(DNA, i)
    return a

def MedianString(Dna, k):
    distance = float('inf')
    Patterns = AllStrings(k)
    for i in range(len(Patterns)):
        Pattern = Patterns[i]
        d = DistanceBetweenPatternAndStrings(Pattern, Dna)
        if distance > d:
            distance = d
            Median = Pattern
    return Median

with open('dataset_5164_1.txt', 'r') as file:
    lines = file.readlines()
Pattern = lines[0].rstrip()
Dna = lines[1].rstrip().split(' ')

print(MedianString(Pattern, 6))