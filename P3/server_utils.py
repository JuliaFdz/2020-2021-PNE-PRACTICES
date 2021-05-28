from Seq1 import Seq
import colorama
import termcolor

def print_colored(message, color):
    colorama.init(strip="False")
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace('\n', '').replace('\r', '')


def ping(cs):
    print_colored('Print', 'green')
    response = 'OK\n'
    print(response)
    cs.send(str(response).encode())

def get(cs, list_sequences, seq_number):
    print_colored('GET', 'yellow')
    try:
        response = list_sequences[int(seq_number)] + '.\n'
        print(response)
    except IndexError:
        response = 'Error: no sequence with index' + str(seq_number) + '.\n'
        print(response)
    cs.send(response.encode())

def info(argument, cs):
    print_colored("INFO", "yellow")
    list_bases = ["A", "C", "T", "G"]
    argument = Seq(argument.replace('"', ""))
    t_l = Seq.len(argument)
    count_list = []
    percentage_list = []
    for base in list_bases:
        count_list.append(argument.count_base_1(base))
    for i in range(0, len(count_list)):
        percentage_list.append(count_list[i] * 100 / t_l)
    response = f"""Sequence: {argument}
    Total length: {t_l}
    A: {count_list[0]} ({percentage_list[0]}%)
    C: {count_list[1]} ({percentage_list[0]}%)
    G: {count_list[2]} ({percentage_list[0]}%)
    T: {count_list[3]} ({percentage_list[0]}%)"""
    cs.send(response.encode())
    print(response)

