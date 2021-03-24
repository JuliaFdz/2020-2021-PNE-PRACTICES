from Client0 import Client
from pathlib import Path

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = '127.0.0.1'
PORT = 6132
c = Client(IP, PORT)
print(c.talk('Sending the U5 Gene to the server...'))
print(c.talk(Path('U5').read_text()))
# reading the content of the file as a str
