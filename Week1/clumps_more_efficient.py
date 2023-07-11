#first way, less efficient

#makes a dictionary with frequency and positions of each k-mer
def FrequencyTable(Text, k):
    freqMap = {}
    for i in range(len(Text) - int(k)):
        Pattern = Text[i:i+int(k)]
        if Pattern not in freqMap:
            freqMap[Pattern] = []
            freqMap[Pattern].append(1)
            freqMap[Pattern].append(i)
        else:
            freqMap[Pattern][0] += 1
            freqMap[Pattern].append(i)
        print(Pattern)
        print(freqMap[Pattern])
    return freqMap


def FindClumps(Text, k, L, t):
    Patterns = []
    n = Text
    for  i in range(len(n) - int(L)):
        Window = Text[i:i+int(L)]
        freqMap = FrequencyTable(Window, k)
        for s in freqMap:
            if freqMap[s][0] >= int(t):
                Patterns.append(s)
    Patterns = list(set(Patterns))
    print(Patterns)
    return Patterns

with open('dataset_4_5.txt', 'r') as file:
    lines = file.readlines()
DNA = lines[0].rstrip()
print(DNA)
nums = lines[1].rstrip().split()
print(nums)
k = nums[0]
print(k)
L = nums[1]
print(L)
t = nums[2]
print(t)
print(*FindClumps(DNA,k,L,t))





#second way, more efficient

def Mapping(k, DNA):
    Map = {}
    for i in range(len(DNA) - int(k)):
        Pattern = DNA[i:i+int(k)]
        if Pattern not in Map:
            Map[Pattern] = []
            Map[Pattern].append(i)
        else:
            Map[Pattern].append(i)
    return Map


def Clumps(Map, k, t, L):
    for kmer, indices in Map.items():
        if len(Map[kmer]) >= int(t):
            for i in range(len(Map[kmer]) - int(t)):
                if Map[kmer][i+int(t)] - Map[kmer][i+int(t)] + int(k) >= int(L):
                    print('nice')




with open('dataset_4_5.txt', 'r') as file:
    lines = file.readlines()
DNA = lines[0].rstrip()
print(DNA)
nums = lines[1].rstrip().split()
print(nums)
k = nums[0]
print(k)
L = nums[1]
print(L)
t = nums[2]
print(t)
Map = Mapping(k, DNA)
print(Clumps(Map, k, t, L))