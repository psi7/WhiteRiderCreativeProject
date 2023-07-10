# This file implements the main functions of the program
from Bio import SeqIO
from Bio.Seq import reverse_complement, transcribe, back_transcribe, translate
from Bio.SeqUtils import seq3


# inputfile = "media\HPVDNA.fasta"

# this is for non fasta raw txt files that contain special hidden characters like /r or /n


def read_seq(inputfile):
    with open(inputfile, "r") as f:
        seq = f.read()
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")
    return seq

# Reads Dna-Rna sequence of virus from Fasta files


def readSeqBio(inputfile):
    for seq_record in SeqIO.parse(inputfile, "fasta"):
        # print(seq_record.id)
        print(repr(seq_record.seq), len(repr(seq_record.seq)))
        # print(len(seq_record))
        return repr(seq_record.seq)
# Transcibres Dna Sequence to Rna and then computes the sequence of protein


def Mtranslate(ifile):
    dna = readSeqBio(ifile)
    dna = str(dna).upper()
    dna = ''.join([base for base in dna if base in 'ATCG'])
    rna = transcribe(dna)
    protein = translate(rna, table=1, stop_symbol='*', to_stop=True)
    protein_3letter = seq3(protein)
    print(protein_3letter)
    print(transcribe(dna))


# Mtranslate()
