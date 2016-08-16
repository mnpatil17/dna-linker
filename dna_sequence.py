
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

    def __len__(self):
        return len(self._seq_str)

    def __eq__(self, other):
        return self._seq_str == other._seq_str

    def __str__(self):
        return self._seq_str

    @staticmethod
    def get_array_of_dna_sequences(sequence_strs):
        """
        Converts a collection of DNA sequence strings into a list of DNASequence objects.

        :param: sequence_strs - A collection of DNA sequences represented a strings
        :return: A list of DNASequence objects representing the given strings
        """
        return [DNASequence(seq_str) for seq_str in sequence_strs]

    def set_prev_seq(self, prev_seq, overlap_size):
        """
        Establishes a doubly-linked relationship between this DNASequence and the given DNASequence

        :param: prev_seq - The DNASequence that front-overlaps this DNASequence
        :param: overlap_size - The size of front-overlapping
        """
        if prev_seq is None:
            self.prev_seq = None
            self.prev_overlap = 0
        else:
            prev_seq.set_next_seq(self, overlap_size)

    def set_next_seq(self, next_seq, overlap_size):
        """
        Establishes a doubly-linked relationship between this DNASequence and the given DNASequence

        :param: next_seq - The DNASequence that back-overlaps this DNASequence
        :param: overlap_size - The size of back-overlapping
        """
        if next_seq is None:
            self.next_seq = None
            self.next_overlap = 0
        else:
            self.next_seq = next_seq
            next_seq.prev_seq = self
            self.next_overlap = overlap_size
            next_seq.prev_overlap = overlap_size

    def merge_with_next(self):
        """
        Merges this DNASequence object with whatever its next_seq neighbor, and carries over the
        relevant pointers. If self.next_seq is None, returns self.

        :return: The merged DNASequence
        """
        if self.next_seq is None:
            return self

        new_seq_str = self._seq_str + self.next_seq._seq_str[self.next_overlap:]
        return DNASequence(new_seq_str, prev_seq=self.prev_seq, next_seq=self.next_seq.next_seq,
                           prev_overlap=self.prev_overlap, next_overlap=self.next_seq.next_overlap)

    def find_overlaps(self, sequences):
        """
        Finds overlaps with this sequence in a particular set of sequences, and establishes
        the prev_seq and next_seq for this DNASequence and the ones in `sequences`

        :param: sequences - A collection of DNASequence objects to find overlaps with
        """
        for other_sequence in sequences:

            # If both neighbors have been found, this function has done its job
            if self.prev_seq is not None and self.next_seq is not None:
                return
            elif other_sequence == self:
                continue

            if self.next_seq is None:
                does_front_overlap, overlap_len = self.this_front_overlaps_other(other_sequence)
                if does_front_overlap:
                    self.set_next_seq(other_sequence, overlap_len)

            if self.prev_seq is None:
                does_back_overlap, overlap_len = self.this_back_overlaps_other(other_sequence)
                if does_back_overlap:
                    self.set_prev_seq(other_sequence, overlap_len)

    def this_front_overlaps_other(self, other_sequence):
        """
        A function that determines if this DNASequence (self) overlaps other_sequence such that at
        least the trailing half of this DNASequence (self) can be seen in the leading part of
        other_sequence. This notion is called "front-overlapping", and can be used as so:
        "this DNASequence front-overlaps other_sequence".

        :param: self - This DNASequence
        :param: other_sequence - The DNASequence to check for front-overlapping with
        :return: A tuple with types (bool, int). The bool value is True if this DNASequence
                 front-overlaps other_sequence; False otherwise. The int value is the total overlap
                 detected, and is None if the bool value is False

        Also see: DNASequence.this_back_overlaps_other
        """
        # finding the total overall overlap
        total_overlap = None
        for i in range(0, len(self) // 2):
            substr = self._seq_str[i:]                 # look for a substring of the previous string
            try:
                # if the substring is found at the beginning of the other sequence, it is our winner
                if other_sequence._seq_str.find(substr, 0, len(substr)) == 0:
                    total_overlap = len(substr)
                    break
            except ValueError:            # if the substring is not found, try a smaller one
                pass

        front_overlaps = total_overlap > len(self) // 2 and total_overlap > len(other_sequence) // 2
        return front_overlaps, total_overlap

    def this_back_overlaps_other(self, other_sequence):
        """
        A function that determines if this DNASequence (self) overlaps other_sequence such that at
        least the leading half of this DNASequence (self) can be seen in the trailing part of
        other_sequence. This notion is called "back-overlapping", and can be used as so:
        "this DNASequence back-overlaps other_sequence".

        This is the converse of front-overlapping: i.e. "A front-overlaps B" if and only if
        "B back-overlaps A".

        :param: self - This DNASequence
        :param: other_sequence - The DNASequence to check for back-overlapping with
        :return: A tuple with types (bool, int). The bool value is True if this DNASequence
                 back-overlaps other_sequence; False otherwise. The int value is the total overlap
                 detected, and is None if the bool value is False

        Also see: DNASequence.this_front_overlaps_other
        """
        return other_sequence.this_front_overlaps_other(self)
