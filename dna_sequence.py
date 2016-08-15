

class DNASequence:
    """
    An abstraction of a DNA sequence.
    """

    def __init__(self, seq_str, prev_seq=None, next_seq=None, prev_overlap=0, next_overlap=0):
        self._seq_str = seq_str

        self.prev_seq = prev_seq
        self.prev_overlap = prev_overlap

        self.next_seq = next_seq
        self.next_overlap = next_overlap

    # @property
    # def _get_midpoint(self):
    #     """
    #     The midpoint index of this DNA sequence
    #     """
    #     return len(self) // 2

    # def get_first_half(self):
    #     return self._seq_str[:self._get_midpoint]

    # def get_last_half(self):
    #     return self._seq_str[self._get_midpoint:]

    def __len__(self):
        return len(self._seq_str)

    # def reverse(self):
    #     """
    #     :return: A DNASequence that is the reverse of self
    #     """
    #     return DNASequence(self._seq_str[::-1])

    def merge_with_next(self):
        new_seq_str = self._seq_str + self.next_seq._seq_str[self.next_overlap:]
        return DNASequence(new_seq_str, prev_seq=self.prev_seq, next_seq=self.next_seq.next_seq,
                           prev_overlap=self.prev_overlap, next_overlap=self.next_seq.next_overlap)

    def find_overlaps(self, sequences):
        """
        Finds overlaps with this sequence in a particular set of sequences.
        """
        for other_sequence in sequences:

            # If both neighbors have been found, this function has done its job
            if self.prev_seq is not None and self.next_seq is not None:
                return
            elif other_sequence == self:
                continue

            if self.next_seq is not None:
                does_front_overlap, overlap_len = self.this_front_overlaps_other(other_sequence)
                if does_front_overlap:
                    self.next_seq = other_sequence
                    other_sequence.prev_seq = self
                    self.next_overlap = overlap_len
                    other_sequence.prev_overlap = overlap_len

            if self.prev_seq is not None:
                does_back_overlap, _ = self.this_back_overlaps_other(other_sequence)
                if does_back_overlap:
                    other_sequence.next_seq = self
                    self.prev_seq = other_sequence
                    other_sequence.next_overlap = overlap_len
                    self.prev_overlap = overlap_len

    def this_front_overlaps_other(self, other_sequence):
        """
        A function that returns True if this DNASequence (self) overlaps other_sequence such that at
        least the trailing half of this DNASequence (self) can be seen in the leading part of
        other_sequence. This notion is called "front-overlapping", and can be used as so:
        "this DNASequence front-overlaps other_sequence".

        :param: self - This DNASequence
        :param: other_sequence - The DNASequence to check for front-overlapping with
        :return: A tuple with types (bool, int). The bool value is True if this DNASequence
                 front-overlaps other_sequence; False otherwise. The int value is the total overlap
                 detected

        Also see: DNASequence.this_back_overlaps_other
        """
        total_len = len(self) + len(other_sequence)

        total_overlap = 0
        for self_char, other_char in zip(self._seq_str[::-1], other_sequence._seq_str):
            if self_char != other_char:
                break
            total_overlap += 1

        # TODO: might have to confirm this rule
        front_overlaps = total_overlap * 2 >= total_len // 2
        return front_overlaps, total_overlap

    def this_back_overlaps_other(self, other_sequence):
        """
        A function that returns True if this DNASequence (self) overlaps other_sequence such that at
        least the leading half of this DNASequence (self) can be seen in the trailing part of
        other_sequence. This notion is called "back-overlapping", and can be used as so:
        "this DNASequence back-overlaps other_sequence".

        This is the converse of front-overlapping: i.e. "A front-overlaps B" if and only if
        "B back-overlaps A".

        :param: self - This DNASequence
        :param: other_sequence - The DNASequence to check for back-overlapping with
        :return: A tuple with types (bool, int). The bool value is True if this DNASequence
                 back-overlaps other_sequence; False otherwise. The int value is the total overlap
                 detected

        Also see: DNASequence.this_front_overlaps_other
        """
        return other_sequence.this_front_overlaps_other(self)

    def __eq__(self, other):
        return self._seq_str == other._seq_str
