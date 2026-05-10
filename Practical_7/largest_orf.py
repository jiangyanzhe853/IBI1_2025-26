seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

start_codon = 'AUG'
stop_codons = ['UAA', 'UAG', 'UGA']

largest_orf = ''

# Search every possible start codon
for i in range(len(seq) - 2):
    codon = seq[i:i + 3]

    if codon == start_codon:

        # Read sequence in-frame from the start codon
        for j in range(i + 3, len(seq) - 2, 3):
            current_codon = seq[j:j + 3]

            if current_codon in stop_codons:
                orf = seq[i:j + 3]

                if len(orf) > len(largest_orf):
                    largest_orf = orf

                break

print('Longest ORF:', largest_orf)
print('Length:', len(largest_orf), 'nucleotides')