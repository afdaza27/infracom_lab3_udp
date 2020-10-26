import socket


message_from_client = "yo"

bytes_to_send = str.encode(message_from_client)

server_address_port = ("127.0.0.1", 20001)

buffer_size = 1024

file = open("recieve.txt", "wb")

#create a UDP socket at client side

udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
#udp_client_socket.bind(server_address_port)


# send to server using created udp socket

udp_client_socket.sendto(bytes_to_send, server_address_port)

data, addr = udp_client_socket.recvfrom(buffer_size)

try:
    while data:
        file.write(data)
        udp_client_socket.settimeout(2)
        data, addr = udp_client_socket.recvfrom(buffer_size)
except:
    file.close()
    udp_client_socket.close()
    print("file downloaded")