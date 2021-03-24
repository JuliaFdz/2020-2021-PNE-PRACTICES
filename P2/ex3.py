from Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = '127.0.0.1'
PORT = 6132
c = Client(IP, PORT)
#response = c.talk('Message')
#print('Response: ', response)
print('Response: ', c.talk('Message'))

# remember: if the function has a return, print the return or store the return in a variable
