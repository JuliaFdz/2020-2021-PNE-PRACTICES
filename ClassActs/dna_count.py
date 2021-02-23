# Profe ex:
def correct_sequence(dna):
    for c in dna:
        if c != 'A' and c !='C' and c !='G' and c != 'T':
            return False
    return True

def count_bases(dna):
    a, c, t, g = 0, 0, 0, 0
    for ch in dna:
        if ch == 'A':
            a += 1
        elif ch == 'C':
            c += 1
        elif ch == 'G:':
            g += 1
        else:
            t += 1
    return a, c, g, t

dna = input('Introduce the sequence:')
if correct_sequence(dna):
    print('Total lenght:', len(dna))
    a, c, g, t = count_bases(dna)
    print('A: ', a)
    print('C: ', c)
    print('G: ', g)
    print('T:', t)
else:
    print('Not a valid sequence of dna.')
# 2nd way
def reading_file(filename):
    with open(filename, 'r') as f:
        dna = f.read()
        dna = dna.replace('\n','')
    return dna

try:
    dna = reading_file(input('Introduce the filename:'))
    if correct_sequence(dna):
        print('Total lenght:', len(dna))
        a, c, g, t = count_bases(dna)
        print('A: ', a)
        print('C: ', c)
        print('G: ', g)
        print('T:', t)
    else:
        print('Not a valid sequence of dna.')
except FileExistsError:
    print('The file has not been found.')
# if it is from a file u must crate a read file def and incorporate it to the code