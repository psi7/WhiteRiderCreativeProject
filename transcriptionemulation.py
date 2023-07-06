import random

# Define the host DNA sequence and viral DNA sequence
host_dna = "ATCGATCGATCGATCGATCGATCG"
viral_dna = "GCTAGCTAGCTAGCTAGCTAGCTA"

# Choose a random position for viral DNA integration
integration_site = random.randint(0, len(host_dna))

# Extract the section of the host DNA for integration
integration_section = host_dna[integration_site:integration_site + len(viral_dna)]

# Simulate integration by concatenating the host DNA section with viral DNA
integrated_dna = integration_section + viral_dna

# Replace the corresponding section of host DNA with integrated DNA
updated_dna = host_dna[:integration_site] + integrated_dna + host_dna[integration_site + len(viral_dna):]

# Print the updated DNA sequence after integration
print("Host DNA:", host_dna)
print("Integrated DNA:", updated_dna)
