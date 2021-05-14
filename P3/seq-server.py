import socket
import server_utils

list_sequences = ['ATTCTATGGATGACT', 'AACCTTTGAGATCAT', 'ATTGTTCTTCTTACT','AATACTTTTATCCCT', 'AAATTTCTCACTTTA']

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))
count_connections = 0
# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")
client_address_list = []
while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
        client_address_list.append(client_ip_port)
        count_connections += 1 # could be outside
        print('CONNECTION' + str(count_connections) + '.Client IP, PORT: ' + str(client_ip_port))

        # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()


    # -- Read the message from the client
    # -- The received message is in raw bytes
    msg_raw = cs.recv(2048)
    print(msg_raw)

    # -- We decode it for converting it
    # -- into a human-redeable string
    msg = msg_raw.decode()
    formatted_msg = server_utils.format_command(msg)
    print(formatted_msg)

    if formatted_msg == "'PING'":
        server_utils.ping()
        # -- Send a response message to the client
        response = 'ok'
        cs.send(str(response).encode())
    else:
        response = 'NO available command'
        cs.send(str(response).encode())
    # -- Close the data socket
    cs.close()


#echo 2 | nc -w 1 127.0.0.1 8080