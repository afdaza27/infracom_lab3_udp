import socket
import sys

localip = "0.0.0.0"

localport = 20001

buffersize = 1024
address = (localip, localport)

file_name = "test.txt"



# create a datagram socket

udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# bind to address and ip

udp_server_socket.bind((localip, localport))

print("udp server up and listening")

# listen for incoming datagrams

while (True):
    file = open(file_name, "rb")
    data = file.read(buffersize)
    bytes_address_pair = udp_server_socket.recvfrom(buffersize)
    message = bytes_address_pair[0]

    ip_address = bytes_address_pair[1]

    client_message = "Message from client:{}".format(message)
    client_ip = "Client ip address:{}".format(ip_address)
    print("message from client: " + client_message)
    print("client address: " + client_ip)

    #udp_server_socket.sendto(data, ip_address)
    while data:
        if udp_server_socket.sendto(data, ip_address):
            print("sending...")
            data = file.read(buffersize)
    file.close()
