import socket
import time


def main():
    # server IP and port to receive connections from 
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005

    # setup socket connection and bind to local host and port 5005
    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))


    # keep track of original sent time and received time
    formatted_timestamp = 0.0
    formatted_received_time_first = 0.0

    # keep track of bytes received for throughput
    total_bytes_received = 0 

    while True:
        # extract data from socket
        data, addr = sock.recvfrom(9216) # max buffer size set to 9216 bytes

        # convert the byte stream into a string
        encoded_str = str(data.decode())


# call the script
if __name__ == "__main__":
    main()