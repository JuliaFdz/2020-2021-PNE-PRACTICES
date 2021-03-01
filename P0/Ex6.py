import Seq0
FOLDER = './sequences/'  # each dot means a folder
ID = 'U5.txt'

U5_seq = Seq0.seq_read_fasta(FOLDER + ID)[0:20]
reverse = Seq0.seq_reverse(U5_seq)

print('Gene U5:')
print('Frag:', U5_seq)
print('Rev:', reverse)
