import colorama
import termcolor

colorama.init(strip="False")
print("To server:", end="")
print(termcolor.colored("Message", "yellow"))
