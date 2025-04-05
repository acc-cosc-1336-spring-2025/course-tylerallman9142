#

def get_p_distance(list1, list2):
    differences = sum(1 for a, b in zip(list1, list2) if a != b)
    return round(differences / len(list1), 5)

def get_p_distance_matrix(dna_lists):
    size = len(dna_lists)
    matrix = [[0.0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if i != j:
                matrix[i][j] = get_p_distance(dna_lists[i], dna_lists[j])
    return matrix