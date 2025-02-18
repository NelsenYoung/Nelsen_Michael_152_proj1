import socket
import json

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

data = {server_ip: "127.0.0.1", server_port: 65432, message: "ping"}
json_string = json.dumps(data)
encoded_data = json_string.encode('utf-8')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(encoded_data)
    data = s.recv(1024)

print(f"Received {data!r}")