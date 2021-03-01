import Seq0
FOLDER = './sequences/'  # each dot means a folder
ID = 'U5.txt'

U5_seq = Seq0.seq_read_fasta(FOLDER + ID)[0:20]
#reversed(U5_seq)
reverse = Seq0.seq_reverse(U5_seq)

print('the first 20 bases are:', U5_seq)
print('reverse:', reverse)
