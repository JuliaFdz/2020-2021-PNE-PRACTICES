import Seq0

GENE_FOLDER = './sequences/'

gene_list = ['U5', 'ADA', 'FRAT1', 'FXN']
#base_list = ['A', 'C', 'T', 'G']

for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + '.txt')
    print('Gene', gene, ': Most frequent Base:', Seq0.most_frq_base(sequence))
