from Bio.Seq import Seq
from Bio.Alphabet import *



# SEPARATOR FOR EACH CODE
my_seq = Seq("CCCGGAGAGA")
# print(type(my_seq))
attributes = [a for a in dir(my_seq) if not a.startswith("_")]
# print(attributes)

###########################
my_dna = Seq("CCCGGAGAG", generic_dna)
my_rna = Seq("ACCCGUUGU", generic_rna)
my_protein = Seq("AKKKGGGUUULL", generic_protein)
###########################
my_transcript = my_dna.transcribe()
print(my_dna)
print(my_transcript)
print(my_transcript.alphabet)

# print(my_dna.translate(to_stop=True)) #basically stops translating after finding a codon

############################
gene = Seq("ATGGCCATTGTAATGTAG", generic_dna)
# print(gene.translate(cds=True)) ###only translates first start codon till stop codon

############################
f = open("AAD01939.txt", "r")

if f.mode == 'r':
    proteinSequence1 = Seq(f.read(), generic_protein)

print(proteinSequence1.alphabet)

"""""""""
SEQUENCE ALIGNENT
"""""""""

seq1 = Seq("tacggtat", generic_dna)
seq2 = Seq("ggacgtacg", generic_dna)

