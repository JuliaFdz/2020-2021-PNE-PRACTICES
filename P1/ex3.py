# pip install termcolor
from Seq1 import Seq

print('-----EXERCISE 1 -----')
seq = Seq('ACTGA')
print('Sequence ' + str(1) + ': (Length '+ str(seq.len()) + ' ) ' + str(seq))

print('-----EXERCISE 2-3 -----')
s1 = Seq()
s2 = Seq('ACTG')
s3 = Seq('Invalid Sequence')

print('Sequence 1:', s1)
print('Sequence 2:', s2)
print('Sequence 3:', s3)

print('-----EXERCISE 4 -----')
s1 = Seq()
s2 = Seq('ACTG')
s3 = Seq('Invalid Sequence')

print('Sequence ' + str(1) + ': (Length '+ str(s1.len()) + ' ) ' + str(s1))
print('Sequence ' + str(2) + ': (Length '+ str(s2.len()) + ' ) ' + str(s2))
print('Sequence ' + str(3) + ': (Length '+ str(s3.len()) + ' ) ' + str(s3))

