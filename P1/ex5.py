from Seq1 import seq

def print_result(i, sequence):
    print('Sequence' + str(i) + ':(Length ' + str(sequence.len()) + ')' + str(ssequence))
    a, c, t, g = sequence.count_bases()
    print('A:'+ str(a) + 'C:' + str(c) + 'G:' + str(g) + 'T:' + str(t) )

print('-----| Practice 1, Exercise 5 |------')
s1 = Seq()
s2 = Seq('ACTG')
s3 = Seq('Invalid Sequence')
#print('Sequence' + str(1) + ':(Length ' + str(s1.len()) + ')' + str(s1))

list_seq = [ s1, s2, s3]
for i in range(0, len(list_seq)):
    print_result(i, list_seq[i-1])