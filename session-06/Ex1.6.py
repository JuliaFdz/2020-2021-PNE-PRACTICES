import P0.Seq0

class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases

        print("New sequence created!")

    #def is_valid_sequence(self):
    #    print(self.strbases)
    def print_bases(self):
        print(self.strbases)

    @staticmethod
    def static_function(text):
        print(text) # can not work with the attributes


    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """ Calculate the length of the sequence """
        return len(self.strbases)


# --- Main program
s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")

 #-- Printing the objects
print(f"Sequence 1: {s1}")
print(f"  Length: {s1.len()}")
print(f"Sequence 2: {s2}")
print(f"  Length: {s2.len()}")

#s1.print_bases() # class instance
#Seq.static_function('hello') #class definition

# check if the method is going to be used a lot
# self is personal to each instance

# RUN python Ex1.6.py
