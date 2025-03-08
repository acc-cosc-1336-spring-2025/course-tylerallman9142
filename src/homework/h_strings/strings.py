#

def get_hamming_distance(dna1, dna2):
    if len(dna1) != len(dna2):
        raise ValueError("DNA strings must be of equal length")
    count = 0
    i = 0
    while i < len(dna1):
        if dna1[i] != dna2[i]:
            count += 1
        i += 1
    return count

def get_dna_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    result = ""
    i = len(dna) - 1
    while i >= 0: 
        result += complement[dna[i]]
        i -= 1
    return result