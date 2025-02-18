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

        # payload data starts on index 20
        data_start = 14

        # print packet number, IP address (local host), and check for final packet
        print("\npacket number: " + encoded_str[:5])
        print("IP address: " + encoded_str[5:14])

        
        if int(encoded_str[:5]) == 0: # decode first packet
            # [packet number: 5 chars][IP address: 9 chars ]([time stamp: 17 chars])[message]

            # track the time the first packet was received
            received_time = time.time()
            formatted_received_time_first = float(f"{received_time:.10f}"[:17])

            # first index of payload
            data_start = 31

            # what time the data was sent from client
            print("time stamp: " + encoded_str[14:31]) 
            timestamp = float(encoded_str[14:31])

            # keep track of the time to measure throughput, make sure it has exactly 17 digits of precision
            formatted_timestamp = float(f"{timestamp:.10f}"[:17])

            
            # what time the data was received (first packet)
            print("recieved on: " + str(formatted_received_time_first) +  " which is: " + str(time.ctime(formatted_received_time_first)))



        elif encoded_str[14:26] == "final packet": # decode final packet
            # [packet number: 5 chars][IP address: 9 chars ]([final packet: 12 chars])[message]

            # calculate the throughput only when we have recieved all messeages
            cur_time = time.time()
            formatted_curr_time = float(f"{cur_time:.10f}"[:17])

            # print that final packet has been received
            print("final packet received")

            # first index of the payload
            data_start = 26

            # difference of time from first packet to last
            time_diff = formatted_curr_time - formatted_received_time_first

            # what time the data was sent from client
            print("timestamp from client: " + str(formatted_timestamp) + " which is: " + str(time.ctime(formatted_timestamp)))

            # print out the times for when the first and last packet were received
            print("first packet recieved time: " + str(formatted_received_time_first) + " which is: " + str(time.ctime(formatted_received_time_first)))
            print("last packet received time: " + str(formatted_curr_time) + " which is: " + str(time.ctime(formatted_curr_time)))
            print("time difference: " + str(time_diff) + " seconds")
            print("total bytes received: " + str(total_bytes_received) + " bytes")

            # calculate the throughput which is the total number of kilobytes sent divided by the time difference
            throughput = (total_bytes_received/1000) / time_diff
            print("throughput: " + str(throughput) + " kilobytes/second")

            # send the throughput back to the client
            sock.sendto(str(throughput).encode(), addr)

            
        # print out the payload as a byte object
        print("data: ", (encoded_str[data_start:]).encode('utf-8'))

        # update the total bytes received
        total_bytes_received += len(data)

# call the script
if __name__ == "__main__":
    main()