#from Seq_fun import Seq
from Seq1 import Seq
import colorama
import termcolor
from jinja2 import Template
from pathlib import Path

def print_colored(message, color):
    colorama.init(strip="False")
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace('\n', '').replace('\r', '')

def read_template_html_file(filename):
    content = Template(Path(filename).read_text())
    return content

def ping(cs):
    print_colored('Print', 'green')
    response = 'OK\n'
    print(response)
    cs.send(str(response).encode())

def get( list_sequences, seq_number):

    #sequence = list_sequences[int(seq_number)]
    context = {
        'number' : seq_number,
        'sequence': list_sequences[int(seq_number)],
    }
    contents = read_template_html_file('HTML/get.HTML').render(context=context)
    return contents



def info(sequence):
    list_bases = ["A", "C", "T", "G"]
    sequence = Seq(sequence.replace('"', ""))
    t_l = Seq.len(sequence)
    count_list = []
    percentage_list = []
    for base in list_bases:
        count_list.append(sequence.count_base_1(base))
    for i in range(0, len(count_list)):
        percentage_list.append(count_list[i] * 100 / t_l)
    context = {
        "sequence": sequence,
        "result": {
            "length": t_l, "bases": {
                "A": str(count_list[0]) + " (" + str(percentage_list[0]) + "%)",
                "C": str(count_list[1]) + " (" + str(percentage_list[1]) + "%)",
                "T": str(count_list[2]) + " (" + str(percentage_list[2]) + "%)",
                "G": str(count_list[3]) + " (" + str(percentage_list[3]) + "%)"
            }
        },
        "operation": "Info"
    }
    contents = read_template_html_file("HTML/operation.HTML").render(context=context)
    return contents

def comp(sequence):
    sequence = Seq(sequence.replace('"', ""))
    comp_seq = str(Seq.seq_complement(sequence))
    context = {
        "sequence": sequence,
        "result": comp_seq,
        "operation": "Comp"
    }
    contents = read_template_html_file("HTML/operation.HTML").render(context=context)
    return contents

def rev(sequence):
    argument = Seq(sequence.replace('"', ""))
    rev_seq = str(Seq.seq_reverse(argument))
    context = {
        "sequence": sequence,
        "result": rev_seq,
        "operation": "Rev"
    }
    contents = read_template_html_file("HTML/operation.HTML").render(context=context)
    return contents



def gene(gene):
    PATH = "./Sequences/" + gene + ".txt"
    s1 = Seq()
    s1.seq_read_fasta(PATH)
    context = {
        "gene_name": gene,
        "gene_contents": s1.strbases
    }
    contents = read_template_html_file("HTML/gene.HTML").render(context=context)
    return contents

def list(list_number, list):
    i = 0
    names = []
    end = 1
    while i <= int(list_number):
        names.append(list[i])
        context = {
            "list_number": list_number,
            'species': names,
            'end': end
        }
        i += 1
        end += 1
    contents = read_template_html_file('HTML/list.html').render(context=context)
    return contents
def karyotype(specie, list):
    kary = ''
    if specie == list[0]:
        kary = ['http://www.ensembl.org/Homo_sapiens/Location/Genome',1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 'x', 'y']
    elif specie == list[1]:
        kary = ['http://www.ensembl.org/Felis_catus/Location/Genome','A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'B4','C1', 'C2', 'D1', 'D2', 'D3', 'D4','E1', 'E2', 'E3', 'F1', 'F2', 'x']
    elif specie == list[2]:
        kary = ['http://www.ensembl.org/Mus_musculus/Location/Genome', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 'x', 'y']
    elif specie == list[3]:
        kary = ['Not provided']
    elif specie == list[4]:
        kary = ['http://www.ensembl.org/Balaenoptera_musculus/Location/Genome',1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 'x', 'y']
    elif specie == list[5]:
        kary = ['http://www.ensembl.org/Gorilla_gorilla/Location/Genome',1, '2A', '2B',3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 'x']
    elif specie == list[6]:
        kary = ['http://www.ensembl.org/Parus_major/Location/Genome',1, 2, 3, 4, '4A', 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, '25LG1', '25LG2', 26, 27, 28, 'LGE22', 'Z']
    elif specie == list[7]:
        kary = ['http://www.ensembl.org/Ictalurus_punctatus/Location/Genome', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
    elif specie == list[8]:
        kary = ['http://www.ensembl.org/Sciurus_vulgaris/Location/Genome', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 'x', 'y']
    elif specie == list[9]:
        kary = ['http://www.ensembl.org/Danio_rerio/Location/Genome', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

    context = {
        "specie": specie,
        'karyotype': kary
    }
    contents = read_template_html_file('HTML/karyotype.html').render(context=context)
    return contents
def length( specie, chromosome, list):
    direccion = ''
    if specie == list[0]:
        kary = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 'x', 'y']
        while True and i < len(kary):
            i = 0
            if chromosome == str(kary[i]):
                direccion = 'http: // www.ensembl.org / Homo_sapiens / Location / Chromosome?r = ' + str(chromosome)
                False
            else:
                i += 1
    elif specie == list[1]:
        kary = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'B4', 'C1',
                'C2', 'D1', 'D2', 'D3', 'D4', 'E1', 'E2', 'E3', 'F1', 'F2', 'x']
        while True and i < len(kary):
            i = 0
            if chromosome == str(kary[i]):
                direccion = 'http://www.ensembl.org/Felis_catus/Location/Chromosome?r=' + str(chromosome)
                False
            else:
                i += 1
    elif specie == list[2]:
        kary = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 'x', 'y']
        while True and i < len(kary):
            i = 0
            if chromosome == str(kary[i]):
                direccion = 'http://www.ensembl.org/Mus_musculus/Location/Chromosome?r=' + str(chromosome)
                False
            else:
                i += 1
    elif specie == list[3]:
        kary = ['Not provided']
        while True and i < len(kary):
            i = 0
            if chromosome == str(kary[i]):
                direccion == 'error'
                False
            else:
                i += 1
    elif specie == list[4]:
        kary = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 'x', 'y']
        while True and i < len(kary):
            i = 0
            if chromosome == str(kary[i]):
                direccion = 'http://www.ensembl.org/Balaenoptera_musculus/Location/Chromosome?r=' + str(chromosome)
                False
            else:
                i += 1
    elif specie == list[5]:
        kary = [ 1, '2A', '2B', 3, 4, 5, 6, 7, 8, 9, 10, 11,
                12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 'x']
        while True and i < len(kary):
            i = 0
            if chromosome == str(kary[i]):
                direccion = 'http://www.ensembl.org/Gorilla_gorilla/Location/Chromosome?r=' + str(chromosome)
                False
            else:
                i += 1
    elif specie == list[6]:
        kary = [1, 2, 3, 4, '4A', 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, '25LG1', '25LG2', 26, 27, 28, 'LGE22', 'Z']
        while True and i < len(kary):
            i = 0
            if chromosome == str(kary[i]):
                direccion = 'http://www.ensembl.org/Parus_major/Location/Chromosome?r=' + str(chromosome)
                False
            else:
                i += 1
    elif specie == list[7]:
        kary = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
        while True and i < len(kary):
            i = 0
            if chromosome == str(kary[i]):
                direccion = 'http://www.ensembl.org/Ictalurus_punctatus/Location/Chromosome?r=' + str(chromosome)
                False
            else:
                i += 1
    elif specie == list[8]:
        kary = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 'x', 'y']
        while True and i < len(kary):
            i = 0
            if chromosome == str(kary[i]):
                direccion = 'http://www.ensembl.org/Sciurus_vulgaris/Location/Chromosome?r=' + str(chromosome)
                False
            else:
                i += 1

    elif specie == list[9]:
        kary = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        while True and i < len(kary):
            i = 0
            if chromosome == str(kary[i]):
                direccion = 'http://www.ensembl.org/Danio_rerio/Location/Chromosome?r=' + str(chromosome)
                False
            else:
                i += 1
    context = {
        'Specie': specie,
        "Chromosome": chromosome,
        'Direction': direccion
    }
    contents = read_template_html_file('HTML/length.html').render(context=context)
    return contents