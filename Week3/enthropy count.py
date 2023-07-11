import math

Motifs = [
"TCGGGGGTTTTT",
"CCGGTGACTTAC",
"ACGGGGATTTTC",
"TTGGGGACTTTT",
"AAGGGGACTTCC",
"TTGGGGACTTCC",
"TCGGGGATTCAT",
"TCGGGGATTCCT",
"TAGGGGAACTAC",
"TCGGGTATAACC"
]

counts = [0, 0, 0, 0] #(A, T, G, C)
enthropy = 0

for pos in range(0, len(Motifs[0])):
    for n in range(0, len(Motifs)):
        if Motifs[n][pos] == 'A':
            counts[0] += 1
        if Motifs[n][pos] == 'T':
            counts[1] += 1
        if Motifs[n][pos] == 'G':
            counts[2] += 1
        if Motifs[n][pos] == 'C':
            counts[3] += 1
    print(counts)

    for count in counts:
        try:
            log = count/10*math.log2(count/10)
            enthropy -= log
        except ValueError:
            continue
    counts = [0,0,0,0]
    
print(enthropy)
