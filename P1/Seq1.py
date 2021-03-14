import P0.Seq0

class Seq:
    """A class for representing sequences"""
    NULL_SEQUENCE = 'NULL'
    INVALID_SEQUENCE = 'ERROR'

    def __init__(self, strbases=NULL_SEQUENCE):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        if strbases == Seq.NULL_SEQUENCE:
            print('Null seq created')
        else:
            if Seq.is_valid_sequence_2(strbases):
                print('New seq has been created')
                self.strbases = strbases
            else:
                self.strbases = Seq.INVALID_SEQUENCE
                print('INCORRECT seq detected')


    def print_bases(self):
        print(self.strbases)

    @staticmethod
    def is_valid_sequence_2(bases):
        for c in bases:
            if c != 'A' and c != 'C' and c != 'G' and c != 'T':
                return False
        return True

    def is_valid_sequence(self):
        for c in self.strbases:
            if c != 'A' and c != 'C' and c != 'G' and c != 'T':
                return False
        return True
    @staticmethod
    def print_seq(list_sequences):
        for i in range(0, len(list_sequences)):
            print('Sequences', i,':(length:', list_sequences[i].len(), ')', list_sequences[i])



    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """ Calculate the length of the sequence """
        if self.strbases == Seq.NULL_SEQUENCE:
            return 0
        else:
            return len(self.strbases)


    def count_bases(self): #null seq does not work
        a, c, g, t = 0, 0, 0, 0
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
              return a, c, g, t
        else:
            for ch in self.strbases:
                if ch == "A":
                    a += 1
                elif ch == "C":
                    c += 1
                elif ch == "G":
                    g += 1
                elif ch == "T":
                    t += 1
            return a, c, g, t
    def count(self):
        a, c, t, g, = self.count_bases()
        return {'A': a, 'C' : c, 'G': g, 'T' : t }
    def reverse(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return 'Null'
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return 'Invalid Sequence' #Seq.INVALID_SEQUENCE
        else:
            return self.strbases[::-1]




def test_sequence():
    s1 = Seq()
    s2 = Seq('ACTG')
    s3 = Seq('Invalid Sequence')
    return s1, s2, s3

# tuple of 3 things -> list-> able to be iterate