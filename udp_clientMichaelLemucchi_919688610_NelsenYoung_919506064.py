import socket
import sys
import random 
import string
import time

def main():
    # try to find the current time
    curr_time = time.time()
    # should be the length of the random payload
    mb_to_send = int(sys.argv[1])
    payload_len = mb_to_send * 1000000 # convert from bytes to megabytes

    # generate the random payload
    random_payload = ''.join(random.choices(string.ascii_letters + string.digits, k=payload_len))
    
    # combine time and payload data
    data_packet = str(curr_time) + random_payload
    

    UDP_IP = "127.0.0.1" # local host
    UDP_PORT = 5005 # client request port
    
    # separate packets by every 9000 and preface each packet with packet # and host IP
    fragment_size = 9000 

    # iterate through the entirety of the data, account for off by 1 offset
    num_fragments = (int(len(data_packet)) / fragment_size) + 1

    for i in range(int(num_fragments)):

        # convert the string message into a byte object
        current_fragment = str(i) + UDP_IP + data_packet[i*fragment_size: fragment_size*(i+1)]
        MESSAGE = current_fragment.encode("utf-8")
        
        print("UDP target IP: %s" % UDP_IP)
        print("UDP target port: %s" % UDP_PORT)
        print("message: %s" % MESSAGE)

        sock = socket.socket(socket.AF_INET, # Internet
                           socket.SOCK_DGRAM) # UDP
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))


if __name__ == "__main__":
    main()