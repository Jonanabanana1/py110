"""
P:
Given 2 strands of DNA, compute the hamming distance
Create a class named DNA that accepts a string as the dna strand

The class will include an instance method named hamming_distance that accepts a string to compare and calculate the hamming distance compared to the original string

Hamming distance = Total sum of differences between two dna strands calculated by checking in each position if they are the same character

If the two dna strands have different lengths, compute the hamming distance over the shorter length

E:
    ABCDE
    ABDDE = 1 hamming distance

    ABCDEFG
    ABC = 0 hamming distance

    ABCDEFG
    ACC = 1 hamming distance

D:
    Strings, compare each character in the string with the other character in the other dna string

A:
    1) Check if two dna strings are different length
        If Yes:
            Set iteration length equal to length of smaller dna
    2) Iterate over each character in both strings and compare the characters for equality.
    3) Whenever something doesn't match, increment hamming distance by 1
    4) Return the hamming distance

"""


class DNA:
    def __init__(self, strand) -> None:
        self.strand = strand

    def hamming_distance(self, other_strand):
        iteration_len = min(len(self.strand), len(other_strand))
        distance = 0

        for idx in range(iteration_len):
            if self.strand[idx] != other_strand[idx]:
                distance += 1

        return distance
