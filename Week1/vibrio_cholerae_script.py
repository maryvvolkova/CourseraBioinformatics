from Bio.Seq import Seq

with open('Vibrio_cholerae.txt', 'r') as file:
    positions = []
    lines = file.readlines()
    Pattern = 'ATGATCAAG'
    DNA = lines[0].rstrip()
    p_len = len(Pattern)
    print('before cycle')
    for i in range(len(DNA)):
        print('in cycle')
        if DNA[i:i+p_len] == Pattern:
            positions.append(i)
    print('after cycle')

print(*positions)