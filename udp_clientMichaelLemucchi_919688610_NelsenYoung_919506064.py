import socket
import sys
import random 
import string
import time

def main():
    # try to find the current time
    curr = time.time()
    # should be the length of the random payload
    payload_len = int(sys.argv[1]) * 1000000 # convert from bytes to megabytes
    random_payload = ''.join(random.choices(string.ascii_letters + string.digits, k=payload_len))
    
    # combine time and payload data
    data_packet = str(curr) + random_payload

    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005
    MESSAGE = data_packet.encode("utf-8")


    print("UDP target IP: %s" % UDP_IP)
    print("UDP target port: %s" % UDP_PORT)
    print("message: %s" % MESSAGE)

    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))


if __name__ == "__main__":
    main()