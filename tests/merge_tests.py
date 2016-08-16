import unittest
from dna_sequence import DNASequence


class MergeTests(unittest.TestCase):
    """
    Tests the ability to merge two tests
    """

    def _establish_next_relationship(self, first_seq, second_seq, overlap_size):
        first_seq.next_seq = second_seq
        second_seq.prev_seq = first_seq
        first_seq.next_overlap = overlap_size
        second_seq.prev_overlap = overlap_size

    def test_simple_merger(self):
        seq_a = DNASequence('AAAATTTT')
        seq_b = DNASequence('TTTTGGGG')
        self._establish_next_relationship(seq_a, seq_b, 4)

        merged_seq = seq_a.merge_with_next()
        expected_merged_seq = DNASequence('AAAATTTTGGGG')
        assert merged_seq == expected_merged_seq, \
            'Merged sequence should be {0} but was {1}'.format(expected_merged_seq, merged_seq)
