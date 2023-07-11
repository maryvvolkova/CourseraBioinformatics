from Bio.Seq import Seq

with open('11111.txt', 'r') as file:
    lines = file.read()
    DNA = lines.rstrip()
    DNA_2 = Seq(DNA)
    print(DNA_2.reverse_complement())