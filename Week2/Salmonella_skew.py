import numpy as np
import matplotlib.pyplot as plt
import re

def readFasta (f: str):
    """
    Reads a fasta file and
    Returns a dictionary with ID as key and sequence as value.
    """
    fastaFile = open(f, 'r')
    fastaLines = fastaFile.readlines()
    seqID = "" 
    seq = ""
    fastaSeqs = {}
    for line in fastaLines:
        if line.startswith('>'):
            fastaSeqs[seqID] = seq
            seqID = line.rstrip().removeprefix('>')
            seq = ""
        else:
            seq += line.rstrip()
    fastaSeqs[seqID] = seq
    fastaSeqs.pop('')
    fastaFile.close()

    return fastaSeqs

DNA = list(readFasta('Salmonella_enterica.txt').values())[0]

#find and keep G and C positions
matches = re.finditer(r"[GC]", DNA)
pos_arr = [match.span()[0] for match in matches]

DNA = DNA.replace('\n', '').replace('G','1 ').replace('C','-1 ').replace('A','0 ').replace('T','0 ')
DNA_arr = np.fromstring(DNA, sep=' ')

#counting
plot_arr = np.cumsum(DNA_arr)
min_pos = plot_arr.argmin()
print(min_pos)

plt.figure(figsize=(10,10))
plt.plot(pos_arr, plot_arr[pos_arr],"-")
plt.xlabel("position")
plt.ylabel("GC diff")
plt.show()