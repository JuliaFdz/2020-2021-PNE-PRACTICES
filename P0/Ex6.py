import Seq0
FOLDER = './sequences/'  # each dot means a folder
ID = 'U5.txt'

U5_seq = Seq0.seq_read_fasta(FOLDER + ID)
#reversed(U5_seq)
reverse = Seq0.seq_reverse(U5_seq[0:20])

print('the first 20 bases are:', U5_seq[0:20])
print('reverse:', reverse)