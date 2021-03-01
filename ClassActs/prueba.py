#def seq_reverse(seq):
#    return reversed(seq)


def seq_complement2(seq):
    gene_dict = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    new_seq = ''
    for d in seq:
        new_seq += gene_dict[d]
    return new_seq

seq = 'ATCG'
print(seq_complement2(seq))