import socket
import json

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port used by the server

# create a socket connection for the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    # connect to the proxy to accept in information
    with conn:
        print(f"Connected by {addr}")
        while True:
            # Data sent by the proxy to the server
            data = conn.recv(1024)
            
            if not data:
                break
            

            # Decode data and print
            decoded_data = data.decode('utf-8')
            print(decoded_data)


            # Modify message and send back to client
            json_string = json.loads(decoded_data)

            # Confirm the server IP again
            if json_string['server_ip'] == "127.0.0.1":
                print("Host IP: 127.0.0.1")

            
            new_message = "pong"
            json_string['message'] = new_message

            # Encode and send
            encoded_data = json.dumps(json_string)
            encoded_data = encoded_data.encode('utf-8')

            conn.sendall(encoded_data)