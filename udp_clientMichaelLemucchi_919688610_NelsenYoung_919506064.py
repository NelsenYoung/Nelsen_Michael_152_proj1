import socket
import sys
import random 
import string
import time

def main():
    # calculate the amount of bytes to send to the server
    mb_to_send = int(sys.argv[1])

    # convert from bytes to megabytes
    payload_len = mb_to_send * 1000000 

    # generate a random payload (letters, digits, and any punctuation marks)
    random_payload = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=payload_len))
    
    # IP for communicating with server
    UDP_IP = "127.0.0.1" 

    # server port that clients send requests to
    UDP_PORT = 5005 
    

    # separate packets by every 9000 bytes
    fragment_size = 9000

    # iterate through the entirety of the data, account for off by 1 offset
    num_fragments = (int(len(random_payload)) / fragment_size) + 1

    # calculate current time
    curr_time = time.time()

    # iterate through the data num_fragment times
    for i in range(int(num_fragments)):
        # encode the last fragment
        if(i == int(num_fragments) - 1):
            # packet number , client IP, decode "final packet" , fragmented payload  
            current_fragment = str(i).zfill(5) + UDP_IP + "final packet" + random_payload[fragment_size*i: fragment_size*(i+1)]
        elif(i == 0): # encode the first fragment
            # packet number, client IP, the current time, fragmented payload
            formatted_time = f"{curr_time:.10f}"[:17] # make sure the time is exactly 17 digits for consistency
            current_fragment = str(i).zfill(5) + UDP_IP + str(formatted_time) + random_payload[fragment_size*i: fragment_size*(i+1)]
        else: # encode regular fragments
            # packet number, client IP, fragmented payload
            current_fragment = str(i).zfill(5) + UDP_IP + random_payload[fragment_size*i: fragment_size*(i+1)]

        # encode the current_fragment string into a byte object
        MESSAGE = current_fragment.encode("utf-8")
    
        # state the target IP and port and fragmented payload
        print("UDP target IP: %s" % UDP_IP)
        print("UDP target port: %s" % UDP_PORT)
        print("message: %s\n" % MESSAGE)

        # generate a socket connection and send request
        sock = socket.socket(socket.AF_INET, # Internet
                           socket.SOCK_DGRAM) # UDP
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

    # recieve the throughput from the server
    data, addr = sock.recvfrom(9216) # max buffer size set to 9216 bytes
    print("throughput: " + str(data.decode()))


# call the script
if __name__ == "__main__":
    main()
    