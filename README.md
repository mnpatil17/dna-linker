# DNA Reconstruction
Python program that reconstructs overlapping segments of DNA from a FASTA format file


### Setup

1. Clone the repo
2. `$ cd dna-linker`
3. `$ pip install -r requirements.txt`


### Usage
To use the DNA Reconstruction, be sure you've completed the setup instructions above. Then:

`$ python main.py <path/to/fasta/file>`


### Running Tests
To ensure things are in working order, you can run tests by executing `$ nosetests`.


### Implementation Details

##### Front-Overlapping and Back-Overlapping DNA Sequences
DNA Reconstruction is performed using a two-pronged approach. We define the concepts of
**front-overlapping** and **back-overlapping**. The easiest way to explain this is by example:

```
	(sequence A)  AGTAGTAATAA
	(sequence B)  	  GTAATAAATA
```

In the example above, we can say that sequence A _front-overlaps_ sequence B by 7 characters.
Conversely, we can say that sequence B _back-overlaps_ sequence A by 7 characters.

The methods `DNASequence.this_front_overlaps_other` and `DNASequence.this_back_overlaps_other`
help determine whether a particular `DNASequence` front-overlaps or back-overlaps another.

Since back-overlapping is just the converse of front-overlapping, it is implemented in that manner.
Front-overlapping is implemented by iterating through at most 1/2 of the first sequence and checking
to see if that sequence is a prefix in the second sequence. This is done carefully, without using
the `index` method for strings; instead it uses the `find` method for strings, with tight bounds,
so the search is done in time proportional to the length of the substring in the worst case, but
when a match is not found, it is usually much faster.

Additionally, since this method starts with the largest possible match (the whole first sequence)
and slowly iterates to smaller possible matches, it is guaranteed to find the largest possible
front-overlap between any two sequences.


##### Ordering overlapping `DNASequences`

Once a front-overlapping or back-overlapping relationship has been detected, the `prev_seq` and
`next_seq` pointers in `DNASequence` are appropriately assigned, so as to create a doubly-linked
list. This occurs in `DNASequence.find_overlaps`, which finds both the overlaps for a particular
fragment (or one, if the fragment is a start/end fragment). The method `establish_all_overlaps` in
`main.py` basically runs `DNASequence.find_overlaps` for all the sequences given to it, effectively
constructing the doubly-linked list. It also returns the starting fragement (the fragement which has
no `prev_seq`). At the end of this method, the doubly-linked list is ready to be traversed.


##### Merging overlapping `DNASequences`

Starting with the given starting sequence, the `merge_all_sequences` method in `main.py` merges
together overlapping `DNASequences`, using simple string manipulations. The result of this method is
the solution to the inquiry, wrapped as a `DNASequence` object.

