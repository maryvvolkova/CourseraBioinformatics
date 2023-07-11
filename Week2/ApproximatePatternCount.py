with open('dataset_9_6.txt', 'r') as file:
    lines = file.readlines()
pattern = lines[0].rstrip()
DNA = lines[1].rstrip()
d = lines[2].rstrip()
list = []

def HammingDistance(DNA1, DNA2):
    HD = 0
    for n in range(len(DNA1)):
        if DNA1[n] != DNA2[n]:
            HD += 1
    return HD

def ApproximatePatternCount(DNA, pattern, d):
    list = []
    for i in range(len(DNA)-len(pattern)+1):
        print(i)
        print(pattern)
        print(DNA[i:i+len(pattern)])
        if pattern == DNA[i:i+len(pattern)] or HammingDistance(pattern, DNA[i:i+len(pattern)]) <= int(d):
            list.append(i)
            print('yes')
        else:
            print('no')
    return list

print(len(ApproximatePatternCount(DNA, pattern, d)))
