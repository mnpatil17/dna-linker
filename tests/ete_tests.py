import unittest
from main import concatenate_dna_sequences
from dna_sequence import DNASequence


class EteTests(unittest.TestCase):
    """
    Tests the end-to-end (ETE) functionality of DNA linking on multiple datasets
    """

    def test_ete_simple(self):
        """
        A simple end-to-end test with sequence fragments to start with
        """

        sequences = DNASequence.get_array_of_dna_sequences(
            ['ATTAGACCTG', 'AGACCTGCCG', 'CCTGCCGGAA', 'GCCGGAATAC'])

        expected_result = DNASequence('ATTAGACCTGCCGGAATAC')
        actual_result = concatenate_dna_sequences(sequences)
        assert actual_result == expected_result, \
            'Concatenation should result in {0} but instead resulted in {1}'.format(
                expected_result, actual_result)
