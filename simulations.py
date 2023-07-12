# This file implements the main functions of the program
from Bio import SeqIO
from Bio.Seq import reverse_complement, transcribe, back_transcribe, translate
from Bio.SeqUtils import seq3
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


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


# Function to generate mutated sequence
def mutate_sequence(sequence, mutation_rate):
    mutated_seq = list(sequence)
    for i in range(len(mutated_seq)):
        # Randomly select a base to mutate
        if random.random() < mutation_rate:
            # Generate a random base different from the original
            bases = ['A', 'T', 'C', 'G']
            bases.remove(sequence[i])
            mutated_seq[i] = random.choice(bases)
    return ''.join(mutated_seq)

# Constants - Estimated mutation rates for each virus
mutation_rates = {
    'Human Papillomavirus (HPV)': 0.1,
    'Human Immunodeficiency Virus (HIV)': 0.3,
    'Human T-lymphotropic Virus 1 (HTLV-1)': 0.2,
    'Human T-lymphotropic Virus 2 (HTLV-2)': 0.5
}

# Actual sequences of the viruses
viruses = {
    'Human Papillomavirus (HPV)': ''.join([base for base in str(readSeqBio('media\HPVDNA.fasta')) if base in 'ATCG']),
    'Human Immunodeficiency Virus (HIV)': ''.join([base for base in str(readSeqBio('media\HIVDNA.fasta')) if base in 'ATCG']),
    'Human T-lymphotropic Virus 1 (HTLV-1)': ''.join([base for base in str(readSeqBio('media\HTLV1DNA.fasta')) if base in 'ATCG']),
    'Human T-lymphotropic Virus 2 (HTLV-2)': ''.join([base for base in str(readSeqBio('media\HTLV2DNA.fasta')) if base in 'ATCG'])
}

# Generate mutated sequences for each virus
def mutation():
    mutated_sequences = {}
    for virus, sequence in viruses.items():
        mutated_sequences[virus] = mutate_sequence(sequence, mutation_rates[virus])
        
    # Plot sequence alignments
    fig, ax = plt.subplots(len(viruses), 1, figsize=(6, 4 * len(viruses)), sharex=True)

    for i, (virus, sequence) in enumerate(viruses.items()):
        ax[i].text(0.05, 0.5, sequence, fontsize=14, va='center')
        ax[i].text(0.05, 0.3, mutated_sequences[virus], fontsize=14, va='center', color='red')
        ax[i].set_xlim(0, 1)
        ax[i].set_ylim(0, 1)
        ax[i].axis('off')
        ax[i].set_title(virus)

    plt.tight_layout()
    plt.show()


# Mtranslate()
# mutation()
