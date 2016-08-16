import unittest
from dna_sequence import DNASequence


class OverlapTests(unittest.TestCase):
    """
    Tests the overlapping detection
    """

    def test_simple_overlap_success(self):
        """
        Checks that two sequences front overlap by the correct amount, and checks the converse
        for back overlapping
        """

        seq_a = DNASequence('AAAAAGGG')
        seq_b = DNASequence('GGGTTTTT')
        expected_num_overlap = 3

        # Check front overlapping
        does_front_overlap, num_front_overlap = seq_a.this_front_overlaps_other(seq_b)
        assert does_front_overlap, '{0} should front overlap {1}'.format(seq_a, seq_b)
        assert num_front_overlap == expected_num_overlap, \
            '{0} should front overlap {1} by {2}. Instead it overlaps by {3}'.format(
                seq_a, seq_b, expected_num_overlap, num_front_overlap)

        # Check back overlapping
        does_back_overlap, num_back_overlap = seq_b.this_back_overlaps_other(seq_a)
        assert does_back_overlap, '{0} should back overlap {1}'.format(seq_a, seq_b)
        assert num_back_overlap == expected_num_overlap, \
            '{0} should back overlap {1} by {2}. Instead it overlaps by {3}'.format(
                seq_a, seq_b, expected_num_overlap, num_back_overlap)

    def test_simple_overlap_failure_small_overlap(self):
        """
        Checks to see that two sequences do NOT front overlap, and checks verifies that there is
        a small overlap, but not enough. Additionally, checks the converse for back overlapping
        """

        seq_a = DNASequence('AAAATTTT')
        seq_b = DNASequence('TTGGTTTT')
        expected_num_overlap = 2

        # Check front overlapping
        does_front_overlap, num_front_overlap = seq_a.this_front_overlaps_other(seq_b)
        assert not does_front_overlap, '{0} should NOT front overlap {1}'.format(seq_a, seq_b)
        assert num_front_overlap == expected_num_overlap, \
            '{0} should front overlap {1} by {2}. Instead it overlaps by {3}'.format(
                seq_a, seq_b, expected_num_overlap, num_front_overlap)

        # Check back overlapping
        does_back_overlap, num_back_overlap = seq_b.this_back_overlaps_other(seq_a)
        assert not does_back_overlap, '{0} should NOT back overlap {1}'.format(seq_a, seq_b)
        assert num_back_overlap == expected_num_overlap, \
            '{0} should back overlap {1} by {2}. Instead it overlaps by {3}'.format(
                seq_a, seq_b, expected_num_overlap, num_back_overlap)

    def test_simple_overlap_failure_no_overlap(self):
        """
        Checks to see that two sequences do NOT front overlap, and checks verifies that there is
        no overlap at all. Additionally, checks the converse for back overlapping
        """

        seq_a = DNASequence('AAAATTTT')
        seq_b = DNASequence('GGGGTTTT')
        expected_num_overlap = 0

        # Check front overlapping
        does_front_overlap, num_front_overlap = seq_a.this_front_overlaps_other(seq_b)
        assert not does_front_overlap, '{0} should NOT front overlap {1}'.format(seq_a, seq_b)
        assert num_front_overlap == expected_num_overlap, \
            '{0} should front overlap {1} by {2}. Instead it overlaps by {3}'.format(
                seq_a, seq_b, expected_num_overlap, num_front_overlap)

        # Check back overlapping
        does_back_overlap, num_back_overlap = seq_b.this_back_overlaps_other(seq_a)
        assert not does_back_overlap, '{0} should NOT back overlap {1}'.format(seq_a, seq_b)
        assert num_back_overlap == expected_num_overlap, \
            '{0} should back overlap {1} by {2}. Instead it overlaps by {3}'.format(
                seq_a, seq_b, expected_num_overlap, num_back_overlap)
