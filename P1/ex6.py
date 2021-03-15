import Seq1

def print_result(i, sequence):
    print('Sequence ' + str(i) + ': (Length ' + str(sequence.len()) + ') ' + str(sequence))
    print('Bases:', sequence.count())

print('-----| Practice 1, Exercise 6 |------')
#  for future knowledge
list_sequences = list(Seq1.test_sequence())
for i in range(0, len(list_sequences)):
    print_result(i, list_sequences[i])

# from P1.Seq1 import Seq, test_sequence