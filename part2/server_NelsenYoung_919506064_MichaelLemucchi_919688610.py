import socket
import json

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

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
            
            # Decode data and print
            decoded_data = data.decode('utf-8')
            print(decoded_data)

            # Modify message and send back to client
            json_string = json.loads(decoded_data)
            new_message = "pong"
            json_string['message'] = new_message

            # Encode and send
            encoded_data = json.dumps(json_string)
            encoded_data = encoded_data.encode('utf-8')

            conn.sendall(encoded_data)