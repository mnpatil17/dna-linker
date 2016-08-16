import unittest
from dna_sequence import DNASequence


class MergeTests(unittest.TestCase):
    """
    Tests the ability to merge two DNA sequences
    """

    def test_simple_merger(self):
        """
        Checks the simple merging functionality of two adjacent DNA sequences
        """
        seq_a = DNASequence('AAAATTTT')
        seq_b = DNASequence('TTTTGGGG')
        seq_a.set_next_seq(seq_b, 4)

        merged_seq = seq_a.merge_with_next()
        expected_merged_seq = DNASequence('AAAATTTTGGGG')
        assert merged_seq == expected_merged_seq, \
            'Merged sequence should be {0} but was {1}'.format(expected_merged_seq, merged_seq)
