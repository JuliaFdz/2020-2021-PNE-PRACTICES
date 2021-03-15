from Seq1 import Seq

def print_result(i, sequence):
    print('Sequence ' + str(1) + ': (Length ' + str(sequence.len()) + ' ) ' + str(sequence))
    print('Bases:', sequence.count())
    print('Rev:', sequence.reverse())
    print('Comp: ', sequence.complement())

# como se accedia a otro directorio ??
PROJECT_PATH = './project/'

print('-----| Practice 1, Exercise 10|------')
s1 = Seq()
s1.seq_read_fasta(PROJECT_PATH + 'ADA.txt')
print('Gene', 'ADA.txt', ': Most frequent Base:', Seq.most_frq_base(s1))

#gene_list = ['U5', 'ADA', 'FRAT1', 'FXN']
#base_list = ['A', 'C', 'T', 'G']

#for gene in gene_list:
 #   sequence = Seq1.seq_read_fasta(GENE_FOLDER + gene + '.txt')
  #  print('Gene', gene, ': Most frequent Base:', Seq1.most_frq_base(sequence))