'''def HammingDistance(DNA1, DNA2):
    HD = 0
    for n in range(len(DNA1)):
        if DNA1[n] != DNA2[n]:
            HD += 1
    return HD



def Neighbors(Pattern, d):
    if d == 0:
        return {Pattern}
    if len(Pattern) == 1:
        return list({'A', 'C', 'G', 'T'})
    Neighborhood = set()
    print(Pattern[1:])
    SuffixNeighbors = Neighbors(Pattern[1:], d)
    for Variant in SuffixNeighbors:
        print(Pattern[1:] + ' , ' + Variant)
        if HammingDistance(Pattern[1:], Variant) < d:
            for N in ['A', 'T', 'G', 'C']:
                el = N + Pattern[1:]
                print(el)
                Neighborhood.add(el)
                print('if' + '\n')
        else:
            el = Pattern[0] + Variant
            Neighborhood.add(el)
            print(el)
            print('else' + '\n')
    print (Neighborhood)
    return list(Neighborhood)'''

'''chars = "ACGT"

def neighbors_1(pattern, d):
    assert(d <= len(pattern))

    if d == 0:
        return pattern

    r2 = neighbors_1(pattern[1:], d-1)
    r = []
    for c in chars:
        for r3 in r2:
            if c != pattern[0]:
                r.append(c + r3)

    if (d < len(pattern)):
        r2 = neighbors_1(pattern[1:], d)
        for r3 in r2:
            r.append(pattern[0] + r3)

neighbors = neighbors_1('AAA', 2)
'''

def ImmediateNeighbors(Pattern, d):
        print('entered def')
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
        

'''def IterativeNeighbors(Pattern, d):
        Neighborhood = set()
        Neighborhood.add(Pattern)
        for j in range(d):
            for Pattern in Neighborhood:
                new_pattern = ImmediateNeighbors(Pattern, d)
                Neighborhood.add(new_pattern)
        return Neighborhood'''

def IterativeNeighbors(Pattern, d):
    neighborhood=[Pattern]
    print(neighborhood)
    for j in range(d): #will do 3 times if d = 2
        for string in neighborhood:
            print(string) #AAA
            neighbors_list = ImmediateNeighbors(string, j)
            if len(neighbors_list) > 1:
                for neighbor in neighbors_list:
                    neighborhood.append(neighbor)
            neighborhood=list(set(neighborhood)) #duplicate removal
    return neighborhood

with open('dataset_3014_4.txt', 'r') as file:
    lines = file.readlines()
DNA = lines[0].rstrip()
d = int(lines[1].rstrip())
Neighborhood = IterativeNeighbors(DNA, d)

sorted = Neighborhood.sort()
for n in Neighborhood:
    print(n)

