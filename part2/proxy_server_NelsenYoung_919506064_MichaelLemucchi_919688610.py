import socket
import json

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 12345  # Port used by the client
SERVER_PORT = 65432 # Port used by the server

# Establish a socket connection with the client
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    server_connection = None
    with conn:
        print(f"Connected by {addr}")
        while True:
            # Collect the data from the client
            data = conn.recv(1024)
            
            if not data:
                break
            
            # decode the data and confirm its IP address
            encoded_data = data.decode('utf-8')
            encoded_data = json.loads(encoded_data)

            if encoded_data['server_ip'] != "127.0.0.1":
                print("Error")
                break

            # establish connection with server
            if server_connection is None:
                server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server_connection.connect(((HOST, SERVER_PORT)))

            # send data to server
            print("sending this to server: ")
            print(encoded_data)

            # rename to the server port and send data to server
            encoded_data['server_port'] = SERVER_PORT
            encoded_data = json.dumps(encoded_data)
            encoded_data = encoded_data.encode('utf-8')
            server_connection.sendall(encoded_data)

            # get response from server
            server_response = server_connection.recv(1024)
            
            # decode the server data, rename the port to the client port
            server_data = server_response.decode('utf-8')
            server_jsonstring = json.loads(server_data)
            print(server_jsonstring)
            server_jsonstring['server_port'] = PORT
            server_jsonstring = json.dumps(server_jsonstring)
            server_payload = server_jsonstring.encode('utf-8')
            
            # send data back to client
            print("sending this back to client: ")
            print(server_payload)
            conn.sendall(server_payload)