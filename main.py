from pyfasta import Fasta
from dna_sequence import DNASequence
import sys


def concatenate_dna_sequences(all_sequences):
    """
    Combines all the DNA sequences given into one large DNA sequence, based on the overlapping
    of the DNA sequence

    :param: all_sequences - A list of DNASequence objects in no particular order
    :return: A DNASequence object that is the merged version of all the DNA sequences given
    """
    starting_sequence = establish_all_overlaps(all_sequences)
    return merge_all_sequences(starting_sequence)


def establish_all_overlaps(all_sequences):
    """
    Finds and establishes all the overlapping connections between DNASequences. Returns the first
    sequence in the order.

    :param: all_sequences - A list of DNASequence objects in no particular order
    :return: The first sequence in the established order
    """

    starting_sequence = None
    for sequence in all_sequences:
        sequence.find_overlaps(all_sequences)

        # if both overlaps are not found, then this is an end in the overall DNA sequence
        if sequence.prev_seq is None:
            starting_sequence = sequence

    return starting_sequence


def merge_all_sequences(starting_sequence):
    """
    Merges all DNASequence objects linked to the given starting_sequence

    :param: starting_sequence - The first DNASequence, which, therefore has no previous sequence
    :return: A DNASequence that is the merged version of all DNASequences linked to
             starting_sequence
    """
    curr_sequence = starting_sequence
    while curr_sequence.next_seq is not None:
        curr_sequence = curr_sequence.merge_with_next()

    return curr_sequence


def read_in_fasta_data(file):
    """
    Reads in FASTA data from a given file

    :param: file - A string that is the path to the file to read the fasta data from
    :return: An array of DNASequence objects from the file
    """
    f = Fasta(file)

    all_sequences = set()
    for _, value in f.items():
        all_sequences.add(str(value))

    return DNASequence.get_array_of_dna_sequences(all_sequences)


if __name__ == '__main__':
    print concatenate_dna_sequences(read_in_fasta_data(sys.argv[1]))
