import unittest
from dna_sequence import DNASequence
from main import find_all_overlaps
from random import shuffle


class MakeOverlapTests(unittest.TestCase):
    """
    Tests the correct matching of overlapping DNA sequences
    """

    def setUp(self):
        self.first_seq = DNASequence('ATTAGACCTG')
        self.second_seq = DNASequence('AGACCTGCCG')
        self.third_seq = DNASequence('CCTGCCGGAA')
        self.fourth_seq = DNASequence('GCCGGAATAC')

        self.sequences = [self.first_seq, self.second_seq, self.third_seq, self.fourth_seq]
        shuffle(self.sequences)

    def test_overlapping_with_first_seq(self):
        """
        Checks to see that the first fragment receives the correct pointers after its overlaps are
        found
        """
        self.first_seq.find_overlaps(self.sequences)

        assert self.first_seq.next_seq == self.second_seq, \
            'first_seq\'s next sequence should be second_seq'

        assert self.second_seq.prev_seq == self.first_seq, \
            'second_seq\'s prev sequence should be first_seq'

        assert self.first_seq.prev_seq is None, 'first_seq\'s prev sequence should be None'

    def test_overlapping_with_last_seq(self):
        """
        Checks to see that the last fragment receives the correct pointers after its overlaps are
        found
        """
        self.fourth_seq.find_overlaps(self.sequences)

        assert self.fourth_seq.prev_seq == self.third_seq, \
            'fourth_seq\'s prev sequence should be third_seq'

        assert self.third_seq.next_seq == self.fourth_seq, \
            'third_seq\'s prev sequence should be fourth_seq'

        assert self.fourth_seq.next_seq is None, 'fourth_seq\'s next sequence should be None'

    def test_overlapping_all(self):
        """
        Tests that finding all overlaps results in the correct ordering
        """

        find_all_overlaps(self.sequences)

        # Check first sequence pointers
        assert self.first_seq.prev_seq is None, 'first_seq\'s prev sequence should be None'
        assert self.first_seq.next_seq == self.second_seq, \
            'first_seq\'s next sequence should be second_seq'

        # Check second sequence pointers
        assert self.second_seq.prev_seq == self.first_seq, \
            'second_seq\'s prev sequence should be first_seq'
        assert self.second_seq.next_seq == self.third_seq, \
            'second_seq\'s next sequence should be third_seq'

        # Check third sequence pointers
        assert self.third_seq.prev_seq == self.second_seq, \
            'third_seq\'s prev sequence should be second_seq'
        assert self.third_seq.next_seq == self.fourth_seq, \
            'third_seq\'s next sequence should be fourth_seq'

        # Check fourth sequence pointers
        assert self.fourth_seq.prev_seq == self.third_seq, \
            'fourth_seq\'s prev sequence should be third_seq'

        assert self.fourth_seq.next_seq is None, 'fourth_seq\'s next sequence should be None'
