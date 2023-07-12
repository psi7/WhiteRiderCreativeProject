# This file implements the main functions of the program
from Bio import SeqIO
from Bio.Seq import reverse_complement, transcribe, back_transcribe, translate
from Bio.SeqUtils import seq3
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import PySimpleGUI as sg



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
    logwindow = sg.Multiline(size=(70, 20), font=('Courier bold', 12),text_color="white",auto_size_text=True)
    lprint = logwindow.print
    layout = [[logwindow]]

    # Create the window that prints the protein sequence
    window = sg.Window("Protein Transcription", layout, finalize=True,resizable=True)
    event, values = window.read(timeout=1)
    lprint("Virus MRNA Sequence: \n")
    lprint(transcribe(dna))
    lprint("Virus Protein sequence: \n")
    lprint(protein_3letter)
    if event == sg.WIN_CLOSED:
        window.close()
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
    'Human Papillomavirus (HPV)': 1,
    'Human Immunodeficiency Virus (HIV)': 3,
    'Human T-lymphotropic Virus 1 (HTLV-1)': 2,
    'Human T-lymphotropic Virus 2 (HTLV-2)': 5
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
        
    # Count nucleotides in the initial sequences
    initial_counts = {virus: {nucleotide: sequence.count(nucleotide) for nucleotide in 'ATCG'} for virus, sequence in viruses.items()}

    # Count nucleotides in the mutated sequences
    mutated_counts = {virus: {nucleotide: sequence.count(nucleotide) for nucleotide in 'ATCG'} for virus, sequence in mutated_sequences.items()}

    # Bar plot with sequence chains
    fig, ax = plt.subplots(len(viruses), 2, figsize=(12, 6 * len(viruses)), gridspec_kw={'width_ratios': [3, 1]})

    for i, (virus, sequence) in enumerate(viruses.items()):
        ax[i, 0].bar(initial_counts[virus].keys(), initial_counts[virus].values(), color='green', label='Initial Virus Sequence')
        ax[i, 0].bar(mutated_counts[virus].keys(), mutated_counts[virus].values(), color='red', label='Mutated Virus')
        ax[i, 0].set_title(f'{virus} - Sequence Comparison')
        ax[i, 0].set_xlabel('Nucleotide')
        ax[i, 0].set_ylabel('Count')
        ax[i, 0].legend()

        ax[i, 1].text(0.5, 0.6, sequence, fontsize=12, va='center', ha='center')
        ax[i, 1].text(0.5, 0.4, mutated_sequences[virus], fontsize=12, va='center', ha='center', color='red')
        ax[i, 1].axis('off')

        ax[i, 0].spines['right'].set_visible(False)
        ax[i, 0].spines['top'].set_visible(False)
        ax[i, 0].xaxis.set_ticks_position('bottom')
        ax[i, 0].yaxis.set_ticks_position('left')

        ax[i, 1].spines['right'].set_visible(False)
        ax[i, 1].spines['top'].set_visible(False)
        ax[i, 1].xaxis.set_ticks_position('bottom')
        ax[i, 1].yaxis.set_ticks_position('left')

        plt.setp(ax[i, 0].get_xticklabels(), rotation=45)
        plt.setp(ax[i, 0].get_yticklabels(), rotation=0)

        plt.setp(ax[i, 1].get_xticklabels(), visible=False)
        plt.setp(ax[i, 1].get_yticklabels(), visible=False)

        plt.subplots_adjust(wspace=0.05)

    plt.tight_layout()
    plt.show()


# Mtranslate()
# mutation()
