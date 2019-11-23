from Bio.Seq import Seq
from Bio.Alphabet import *
from  Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist
from Bio import SeqIO

"""""""""""""""""""""""""""""
PUT FILES IN A PROTEIN SEQUENCE
"""""""""""""""""""""""""""""

records = SeqIO.read("sequence1.fasta", "fasta")
records2 = SeqIO.read("sequence2.fasta", "fasta")

homoSapien_seq = records.seq
botFly_seq = records2.seq

print(homoSapien_seq)
print(botFly_seq)

matrix = matlist.blosum62

alignments = pairwise2.align.globalds(homoSapien_seq, botFly_seq, matrix, -10, -0.5)

print(len(alignments))

print("GLOBAL ALIGNMENT ")
print(pairwise2.format_alignment(*alignments[0]) + "\n\n")

f = open("Num3globalAlignment.txt", "w+")

f.write(pairwise2.format_alignment(*alignments[0]))

alignments1 = pairwise2.align.localds(homoSapien_seq, botFly_seq, matrix, -10, -0.5)

print("LOCAL ALIGNMENT")
print(pairwise2.format_alignment(*alignments1[0]))

f = open("Num3localAlignment.txt", "w+")
f.write(pairwise2.format_alignment(*alignments1[0]))

f.close()

