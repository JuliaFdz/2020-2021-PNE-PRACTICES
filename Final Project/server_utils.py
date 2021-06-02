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

