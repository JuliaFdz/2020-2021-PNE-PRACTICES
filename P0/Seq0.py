from pathlib import Path
# path is a function inside the module pathlib // path is a way to open a file
# marca el directorio P0 como root directorio si da error


def seq_ping():
    print('OK')
# since we are texting, no return needed¿?

def take_out_first_line(sequence):
    return sequence[sequence.find('\n') + 1:].replace('\n', '')
# in order to used it in the future

def seq_read_fasta(filename):
    sequence = take_out_first_line(Path(filename).read_text())
    return sequence
    #sequences = sequences[sequences.find('\n') + 1:].replace('\n', '')
    #sequences = sequences.split('\n',1)[1].replace('\n','')   do the same
# we could have used the open file function too

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base) # look for data

# 2 ways: (ex5)
def seq_count0(seq):
    a, c, t, g = 0, 0, 0, 0
    for d in seq:
        if d == 'A':
            a += 1
        elif d == 'C':
            c += 1
        elif d == 'G':
            g += 1
        else:
            t += 1
    return {'A': a, 'C': c, 'G': g, 'T': t}  # ahorra espacio

def seq_count(seq):
    gene_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for d in seq:
        gene_dict[d] += 1
    return gene_dict

# 2nd way, showing u know pgmn´s

def  seq_reverse(seq):
    n = 1
    new_seq = []
    while seq > n:
        new_seq.append(seq[-n])
    return new_seq


