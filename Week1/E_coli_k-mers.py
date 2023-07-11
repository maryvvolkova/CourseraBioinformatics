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
    a = []
    for kmer, indices in Map.items():
        if len(Map[kmer]) >= int(t):
            for i in range(len(Map[kmer]) - int(t) + 1):
                if Map[kmer][i+int(t)-1] - Map[kmer][i] + int(k) <= int(L):
                    print(Map[kmer][i+int(t)-1] - Map[kmer][i] + int(k))
                    a.append(kmer)
    return a



with open('E_coli.txt', 'r') as file:
    lines = file.readlines()
DNA = lines[0].rstrip()
k = 9
L = 500
t = 3
Map = Mapping(k, DNA)
a = Clumps(Map,k,t,L)
s = list(set(a))
print(s)
print(len(s))