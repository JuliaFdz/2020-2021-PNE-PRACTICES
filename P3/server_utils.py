
def print_colored(message, color):
    import termcolor
    import colorama
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace('\n', '').replace('\r', '')


def ping():
    print_colored('PING command', 'green')