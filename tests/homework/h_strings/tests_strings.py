#

import unittest

from src.homework.h_strings.strings import get_hamming_distance
from src.homework.h_strings.strings import get_dna_complement

class Test_Config(unittest.TestCase):

    def test_get_hamming_distance(self):
        str1 = "GAGCCTACTAACGGGAT"
        str2 = "CATCGTAATGACGGCCT"
        #expected_distance = 7
        self.assertEqual(get_hamming_distance(str1, str2), 7)

    def test_get_dna_complement(self):
        dna = "AAAACCCGGT"
        self.assertEqual(get_dna_complement(dna), "ACCGGGTTTT")
