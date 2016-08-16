
def find_all_overlaps(all_sequences):

    starting_sequence = None
    for sequence in all_sequences:
        sequence.find_overlaps(all_sequences)

        # if both overlaps are not found, then this is an end in the overall DNA sequence
        if sequence.prev_seq is None:
            starting_sequence = sequence

    return starting_sequence


def merge_all_sequences(starting_sequence):

    curr_sequence = starting_sequence
    while curr_sequence.next_seq is not None:
        curr_sequence = curr_sequence.merge_with_next()

    return curr_sequence

# if __name__ == '__main__':
#     print merge_all_sequences(find_all_overlaps())
