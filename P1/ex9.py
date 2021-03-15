from Seq1 import Seq

def print_result(i, sequence):
    print('Sequence ' + str(1) + ': (Length ' + str(sequence.len()) + ' ) ' + str(sequence))
    print('Bases:', sequence.count())
    print('Rev:', sequence.reverse())
    print('Comp: ', sequence.complement())

PROJECT_PATH = './project/'

print('-----| Practice 1, Exercise 9 |------')
s1 = Seq()
s1.seq_read_fasta(PROJECT_PATH + 'ADA.txt')
print_result('',s1)