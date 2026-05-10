input_file = '/Users/juanxincai/IBI/IBI1_2025-26/Practical_7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file = 'stop_genes.fa'

stop_codons = ['TAA', 'TAG', 'TGA']


def find_in_frame_stop_codons(sequence):
    """
    Identify which stop codons are present in-frame
    in an ORF beginning with ATG.
    """

    found_stop_codons = set()

    # Search for all possible ATG start codons
    for i in range(len(sequence) - 2):

        if sequence[i:i + 3] == 'ATG':

            # Move in-frame from the ATG codon
            for j in range(i + 3, len(sequence) - 2, 3):
                codon = sequence[j:j + 3]

                if codon in stop_codons:
                    found_stop_codons.add(codon)
                    break

    return sorted(found_stop_codons)


with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:

    gene_name = ''
    sequence_parts = []

    for line in infile:
        line = line.strip()

        # Header line
        if line.startswith('>'):

            # Process previous gene
            if gene_name:
                sequence = ''.join(sequence_parts)
                stops = find_in_frame_stop_codons(sequence)

                if stops:
                    outfile.write(f'>{gene_name} {" ".join(stops)}\n')
                    outfile.write(sequence + '\n')

            # Get gene name only
            header = line[1:]
            gene_name = header.split()[0]

            sequence_parts = []

        else:
            sequence_parts.append(line.upper())

    # Process final gene
    if gene_name:
        sequence = ''.join(sequence_parts)
        stops = find_in_frame_stop_codons(sequence)

        if stops:
            outfile.write(f'>{gene_name} {" ".join(stops)}\n')
            outfile.write(sequence + '\n')

print('Finished writing stop_genes.fa')