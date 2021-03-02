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
    frq_base = ''
    gene_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for d in seq:
        gene_dict[d] += 1
    for n in gene_dict.keys():
        if gene_dict[n] == max(gene_dict.values()):
            frq_base += n + ' '
    return frq_base, max(gene_dict.values())

print(biggest(seq))