#def seq_reverse(seq):
#    return reversed(seq)


def seq_complement2(seq):
    gene_dict = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    new_seq = ''
    for d in seq:
        new_seq += gene_dict[d]
    return new_seq

seq = 'AATCG'
#print(seq_complement2(seq))
def biggest(seq):
    gene_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for d in seq:
        gene_dict[d] += 1
    location = max(gene_dict.values())
    return location
print(biggest(seq))