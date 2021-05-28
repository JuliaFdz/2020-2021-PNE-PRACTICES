def sequence(prueba):
    i = 0
    a = 0
    t = 0
    c = 0
    g = 0
    unknown = []
    while i < len(prueba):
        if prueba[i].upper() == 'A':
            a += 1
        elif prueba[i].upper() == 'T':
            t += 1
        elif prueba[i].upper() == 'C':
            c += 1
        elif prueba[i].upper() == 'G':
            g += 1
        else:
            unknown.append(prueba[i])
        i += 1
    return a, c, t, g, unknown

def print_function(prueba, casa):
    print('Total Length: ', len(prueba))
    print('A: ', casa[0],'\nC: ', casa[1], '\nT: ', casa[2], '\nG: ', casa[3], '\nUnknown characters: ', casa[4])
    return ''
prueba = input('Introduce the Sequence: ')
print(print_function(prueba,sequence(prueba)))

