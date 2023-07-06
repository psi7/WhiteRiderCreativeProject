from Bio.Seq import Seq
from Bio.Alphabet import generic_rna

# Define the mRNA sequences for the viruses
virus_mrna_sequences = {
    'Human Papillomavirus (HPV)': 'ATCGATCGATCG',
    'Human Immunodeficiency Virus (HIV)': 'TTGCTAGCGATG',
    'Helicobacter pylori': 'CGGATGCGATGC',
    'Epstein-Barr Virus (EBV)': 'AGCGATGCATGC'
}

# Eukaryotic cell mRNA sequence after virus infection
eukaryotic_mrna = Seq('ATCGATCGATCG', generic_rna)

# Transcribe the mRNA sequence for each virus
transcribed_sequences = {}
for virus, virus_mrna in virus_mrna_sequences.items():
    virus_mrna_seq = Seq(virus_mrna, generic_rna)
    transcribed_seq = eukaryotic_mrna + virus_mrna_seq
    transcribed_sequences[virus] = transcribed_seq

# Print the transcribed mRNA sequences for each virus
for virus, transcribed_seq in transcribed_sequences.items():
    print(f'{virus}: {transcribed_seq}')
