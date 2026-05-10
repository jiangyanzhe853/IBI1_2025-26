def calculate_protein_mass(sequence):
    # Amino acid residue mass dictionary (monoisotopic)
    aa_mass = {
        'G': 57.02, 'A': 71.04, 'S': 87.03, 'P': 97.05,
        'V': 99.07, 'T': 101.05, 'C': 103.01, 'I': 113.08,
        'L': 113.08, 'N': 114.04, 'D': 115.03, 'Q': 128.06,
        'K': 128.09, 'E': 129.04, 'M': 131.04, 'H': 137.06,
        'F': 147.07, 'R': 156.10, 'Y': 163.06, 'W': 186.08
    }
    total_mass = 0.0
    for aa in sequence:
        if aa not in aa_mass:
            raise ValueError(f"Error: Unknown amino acid symbol '{aa}'")
        total_mass += aa_mass[aa]
    return total_mass

# Example function call (required)
example_sequence = "GASPV"
print("Protein Mass Prediction Example:")
print(f"Mass of sequence {example_sequence} = {calculate_protein_mass(example_sequence)} amu\n")
