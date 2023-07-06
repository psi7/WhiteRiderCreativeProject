import random
import matplotlib.pyplot as plt

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
    'Human Papillomavirus (HPV)': 0.0001,
    'Human Immunodeficiency Virus (HIV)': 0.0003,
    'Helicobacter pylori': 0.0002,
    'Epstein-Barr Virus (EBV)': 0.0005
}

# Actual sequences of the viruses
viruses = {
    'Human Papillomavirus (HPV)': 'ATCGATCGATCG',
    'Human Immunodeficiency Virus (HIV)': 'TTGCTAGCGATG',
    'Helicobacter pylori': 'CGGATGCGATGC',
    'Epstein-Barr Virus (EBV)': 'AGCGATGCATGC'
}

# Generate mutated sequences for each virus
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
