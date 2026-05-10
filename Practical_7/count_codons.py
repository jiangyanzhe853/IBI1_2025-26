import matplotlib.pyplot as plt

input_file = '/Users/juanxincai/IBI/IBI1_2025-26/Practical_7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'

valid_stop_codons = ['TAA', 'TAG', 'TGA']

# Ask user for stop codon
selected_stop = input('Enter a stop codon (TAA, TAG, or TGA): ').upper()

while selected_stop not in valid_stop_codons:
    selected_stop = input('Invalid codon. Enter TAA, TAG, or TGA: ').upper()


# Dictionary for codon counts
codon_counts = {}


# Create all possible codons
bases = ['A', 'T', 'G', 'C']

for base1 in bases:
    for base2 in bases:
        for base3 in bases:
            codon = base1 + base2 + base3
            codon_counts[codon] = 0


# Read fasta file
with open(input_file, 'r') as infile:

    gene_name = ''
    sequence_parts = []

    for line in infile:
        line = line.strip()

        if line.startswith('>'):

            # Process previous sequence
            if gene_name:
                sequence = ''.join(sequence_parts)

                longest_orf_codons = []

                # Search all ORFs
                for i in range(len(sequence) - 2):

                    if sequence[i:i + 3] == 'ATG':

                        current_orf_codons = []

                        for j in range(i, len(sequence) - 2, 3):
                            codon = sequence[j:j + 3]

                            current_orf_codons.append(codon)

                            if codon == selected_stop:

                                # Keep longest ORF only
                                if len(current_orf_codons) > len(longest_orf_codons):
                                    longest_orf_codons = current_orf_codons.copy()

                                break

                # Count codons from longest ORF
                if longest_orf_codons:

                    for codon in longest_orf_codons[:-1]:
                        codon_counts[codon] += 1

            # Start new gene
            gene_name = line[1:].split()[0]
            sequence_parts = []

        else:
            sequence_parts.append(line.upper())

    # Process final gene
    if gene_name:
        sequence = ''.join(sequence_parts)

        longest_orf_codons = []

        for i in range(len(sequence) - 2):

            if sequence[i:i + 3] == 'ATG':

                current_orf_codons = []

                for j in range(i, len(sequence) - 2, 3):
                    codon = sequence[j:j + 3]

                    current_orf_codons.append(codon)

                    if codon == selected_stop:

                        if len(current_orf_codons) > len(longest_orf_codons):
                            longest_orf_codons = current_orf_codons.copy()

                        break

        if longest_orf_codons:

            for codon in longest_orf_codons[:-1]:
                codon_counts[codon] += 1


# Remove codons with zero counts
filtered_codons = {}

for codon, count in codon_counts.items():
    if count > 0:
        filtered_codons[codon] = count


# Print results
print('\nCodon counts upstream of', selected_stop)

for codon, count in sorted(filtered_codons.items()):
    print(codon, count)


# Generate pie chart
plt.figure(figsize=(16, 16))

plt.pie(
    filtered_codons.values(),
    labels=filtered_codons.keys(),
    autopct='%1.1f%%',
    startangle=90,
    labeldistance=1.28,
    pctdistance=0.88,
    textprops={'fontsize': 8}
)

plt.title(
    f'Codon distribution upstream of {selected_stop}',
    fontsize=18
)

output_image = f'codon_usage_{selected_stop}.png'

plt.savefig(
    output_image,
    bbox_inches='tight'
)
plt.show ()
print('\nPie chart saved as', output_image)


