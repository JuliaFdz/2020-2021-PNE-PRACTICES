from Seq1 import test_sequence
from Seq1 import Seq

def print_result(i, sequence):
    print('Sequence' + str(i) + ':(Length ' + str(sequence.len()) + ')' + str(sequence))
    print('Bases:', sequence.count())
    print('Rev:', sequence.reverse())

print('-----| Practice 1, Exercise 7 |------')
#  for future knowledge
list_sequences =  list(test_sequence())          #list(Seq1.test_sequence())
for i in range(0, len(list_sequences)):
    print_result(i, list_sequences[i])
    print()
