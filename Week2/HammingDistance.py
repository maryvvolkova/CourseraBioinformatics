with open('dataset_9_4.txt', 'r') as file:
    lines = file.readlines()
pattern = lines[0].rstrip()
DNA = lines[1].rstrip()
k = lines[2].rstrip()
list = []

def HammingDistance(DNA1, DNA2):
    HD = 0
    for n in range(len(DNA1)):
        if DNA1[n] != DNA2[n]:
            HD += 1
    return HD

for i in range(len(DNA)-len(pattern)+1):
    print(i)
    print(pattern)
    print(DNA[i:i+len(pattern)])
    if pattern == DNA[i:i+len(pattern)] or HammingDistance(pattern, DNA[i:i+len(pattern)]) <= int(k):
        list.append(i)

print(len(pattern))

print(*list)
