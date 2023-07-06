import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

# Create 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot sequence alignments
x = range(len(sequence))
for i, (virus, sequence) in enumerate(viruses.items()):
    y = [i] * len(sequence)
    z = [0] * len(sequence)
    ax.plot(x, y, z, label=virus)

    y = [i] * len(sequence)
    z = [1] * len(sequence)
    ax.plot(x, y, z, label="Mutated " + virus, color='red')

# Set plot labels and title
ax.set_xlabel('Position')
ax.set_ylabel('Virus')
ax.set_zlabel('Sequence')
ax.set_title('Genetic Alterations: Original Sequence vs. Mutated Sequence')

# Adjust the plot layout
ax.view_init(azim=30)
plt.xticks(x)
ax.set_yticks(range(len(viruses)))
ax.set_yticklabels(viruses.keys())

# Add legend
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()
