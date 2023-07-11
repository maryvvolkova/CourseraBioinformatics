'''def ImmediateNeighbors(Pattern):
        Neighborhood = set()
        Neighborhood.add(Pattern)
        for i in range(len(Pattern)):
            symbol = Pattern[i]
            for x in 'ATGC':
                if x != symbol:
                    Neighbor = Pattern[:i] + x + Pattern[i+1:]
                    Neighborhood.add(Neighbor)
        return Neighborhood'''

'''def HammingDistance(DNA1, DNA2):
    HD = 0
    for n in range(len(DNA1)):
        if DNA1[n] != DNA2[n]:
            HD += 1
    return HD'''

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

'''def Neighbors(Pattern, d):
        if d == 0:
            return {Pattern}
        if len(Pattern) == 1 :
            return list({'A', 'C', 'G', 'T'})
        Neighborhood = set()
        SuffixNeighbors = Neighbors(Pattern[1:], d)
        for Variant in SuffixNeighbors:
            if HammingDistance(Pattern[1:], Variant) < d:
                for N in ['A', 'T', 'G', 'C']:
                    el = N + Pattern[1:]
                    Neighborhood.add(el)
            else:
                el = Pattern[0] + Variant
                Neighborhood.add(el)
        return list(Neighborhood)'''


def MaxMap(freqMap):
    values = freqMap.values()
    return max(values)

def FrequentWordsWithMismatches(DNA, k, d):
    Patterns = []
    freqMap = {}
    n = len(DNA)
    for i in range(n - k + 1):
        Pattern = DNA[i:i+k]
        neighborhood = IterativeNeighbors(Pattern, d)
        for neighbor in neighborhood:
            freqMap[neighbor] = freqMap.get(neighbor, 0) + 1


    m = MaxMap(freqMap)
    for Pattern in freqMap:
        if freqMap[Pattern] == m:
            Patterns.append(Pattern)


    return Patterns


def CountFrequency(my_list):
 
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
 
    for key, value in freq.items():
        print ("% d : % d"%(key, value))


from Bio.Seq import Seq
with open('dataset_9_9.txt', 'r') as file:
    lines = file.readlines()
DNA = lines[0].rstrip()
k = int(lines[1].rstrip().split(' ')[0])
d = int(lines[1].rstrip().split(' ')[1])

answer = FrequentWordsWithMismatches(DNA, k, d)
print(k)
print(d)
answer = list(set(answer))
print(answer)


print(CountFrequency(answer))
