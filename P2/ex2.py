from Client0 import Client

PRACTICE = 2
EXERCISE = 2

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = '127.0.0.1'
PORT = 6132
c = Client(IP, PORT)
print(c)
# w/ the str function we are just creating a direct transformation of our class into a str
