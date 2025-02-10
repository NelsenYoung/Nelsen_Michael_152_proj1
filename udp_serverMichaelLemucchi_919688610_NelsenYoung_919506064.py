import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    cur = time.time()
    encoded = str(data).encode('utf-8')
    print("split message: %s" % encoded[:4])
    print("received message: %s" % data)
    print("recieved on: " + str(cur) +  " which is: " + str(time.ctime(cur)))
    print("size of time: " + str(len(str(cur))))