with open('dataset_7_10.txt', 'r') as file:
    lines = file.readlines()
DNA = lines[0].rstrip()
skew = {}
skew[0] = 0

for pos in range(1, len(DNA)+1):
    skew[pos] = skew[pos-1]
    if DNA[pos-1] == 'G':
        skew[pos] += 1
    if DNA[pos-1] == 'C':
        skew[pos] -= 1

res =  [pos for pos in skew if 
        all(skew[temp] >= skew[pos]
        for temp in skew)]

print(*res, sep=' ')