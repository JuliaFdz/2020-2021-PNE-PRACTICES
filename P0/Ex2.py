import Seq0

FOLDER = './sequences/'  # each dot means a folder
ID = 'U5'

U5_seq = Seq0.seq_read_fasta(FOLDER + ID)

#U5_seq = Seq0.seq_read_fasta(ID)
print('the first 20 bases are:', U5_seq[0:20])  # n-1(last)
#print(len(U5_seq[0:20]))   s:20
#print(len(U5_seq[0:21]))   s:21


# if the folder is somewhere else:   go backwards
#FOLDER = '../session-04/'
#U5_seq = Seq0.seq_read_fasta(FOLDER + ID)