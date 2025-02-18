import socket
import json

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 12345  # Port to listen on (non-privileged ports are > 1023)

SERVER_PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            
            if not data:
                break
            
            
            encoded_data = data.decode('utf-8')
            encoded_data = json.loads(encoded_data)

            if encoded_data['server_ip'] != "127.0.0.1":
                print("Error")
                break

            # establish connection with server
            server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_connection.connect(((HOST, SERVER_PORT)))

            # send data to server
            print(encoded_data)
            encoded_data = encoded_data.encode('utf-8')

            server_connection.sendall(encoded_data)

            # get response from server
            server_response = server_connection.recv(1024)
            
            # send data back to client
            conn.sendall(server_response)