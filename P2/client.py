import socket

# in order to run --> cd cdP2 python seq-server.py -->split vertically the terminal --> python seq-server.py
PORT = 6132  # client and server must have same port and IP
IP = "127.0.0.1"

# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes
s.send(str.encode("HELLO FROM THE CLIENT!!!"))

# Receive data from the server
msg = s.recv(2048)
print("MESSAGE FROM THE SERVER:\n")
print(msg.decode("utf-8"))

# Closing the socket
s.close()
