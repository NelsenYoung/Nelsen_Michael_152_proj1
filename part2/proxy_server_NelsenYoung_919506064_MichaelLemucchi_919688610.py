import socket

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
            
            
            encoded_data = data.decode('utf-8')
            if encoded_data['server_ip'] != "127.0.0.1":
                print("Error")
                break

            print(encoded_data)
            encoded_data = encoded_data.encode('utf-8')

            conn.sendall(encoded_data)