import Seq0
FOLDER = './sequences/'
ID = 'U5.txt'

U5_seq = Seq0.seq_read_fasta(FOLDER + ID)[0:20]
complement = Seq0.seq_complement(U5_seq)

print('Gene U5:')
print('Frag:', U5_seq)
print('Comp:', complement)