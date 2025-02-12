import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

# We know that the first 2 characters are b' so we can ignore them
# We know that if the next 4 characters are 0, then the time stamp will come after the IP address
# We know that if the 12 characters after the IP address are "final packet", then the message is the last packet
# We know that the time stamp will be 17 characters long
# So the message structure is as follows: [packet number: 5 chars][IP address: 9 chars ]([time stamp: 17 chars])([final packet: 12 chars])[message]
cur_time = time.time()
recieved_time = 0.0
first_bits_first_packet = "Nelsen"
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    encoded = str(data).encode('utf-8')
    data_start = 19
    encoded_str = str(encoded)
    print(encoded_str[:37])

    #print("split message: %s" % encoded[2:19])
    #print("received message: %s" % data)
    print("packet number: " + encoded_str[5:10])
    print("IP address: " + encoded_str[11:19])
    print("is Final: " + encoded_str[19:31])
    if(int(encoded_str[5:10]) == 0):
        print("time stamp: " + encoded_str[20:35])
        print("recieved on: " + str(cur_time) +  " which is: " + str(time.ctime(cur_time)))
        recieved_time = float(encoded_str[20:35])
        print("recieved time: " + str(time.ctime(recieved_time)))
        first_bits_first_packet = encoded_str[:51]
        data_start = 36
    if(encoded_str[19:31] == "final packet"):
        print("final packet recieved")
        cur_time = time.time()
        data_start = 32
        # Calculate the throughput only when we have recieved all messeages
        time_diff = cur_time - recieved_time
        print("recieved time: " + str(time.ctime(recieved_time)))
        print("current time: " + str(time.ctime(cur_time)))
        print("time difference: " + str(time_diff) + " seconds")
        throughput = ((len(encoded[33:])/1000) + (int(encoded_str[5:10] * 9))) / time_diff
        print("throughput: " + str(throughput) + " bytes/second")
    
    print("first bits: " + first_bits_first_packet)
    print("data: " + encoded_str[data_start:])
