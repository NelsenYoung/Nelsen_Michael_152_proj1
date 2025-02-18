import socket
import json

HOST = "127.0.0.1"  # IP address to establish connection with server
PORT = 12345  # Port used by the client
message = "ping" # message to send

# create the json data object to send to server (through proxy)
data = {'server_ip': HOST, 'server_port': PORT, 'message': message}
json_string = json.dumps(data)
encoded_data = json_string.encode('utf-8')

# create a socket connection with the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        # send over the encoded json data
        s.sendall(encoded_data)
        data = s.recv(1024)
        print(f"Received {data!r}")