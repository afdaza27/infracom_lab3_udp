import socket


localip = "0.0.0.0"

localport = 20001
localport1 = 20002
localport2 = 20003
localport3 = 20004

buffersize = 1024
address = (localip, localport)
address1 = (localip, localport1)
address2 = (localip, localport2)
address3 = (localip, localport3)

nombre_video_1 = "Minecraft.mp4"
nombre_video_2 = "Kraft Punk.mp4"
nombre_video_3 = "Morshu Beatbox.mp4"


# create a datagram socket

udp_server_socket = socket.socket(
    family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_server_socket1 = socket.socket(
    family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_server_socket2 = socket.socket(
    family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_server_socket3 = socket.socket(
    family=socket.AF_INET, type=socket.SOCK_DGRAM)

# bind to address and ip

udp_server_socket.bind(address)
udp_server_socket1.bind(address1)
udp_server_socket2.bind(address2)
udp_server_socket3.bind(address3)

print("udp server up and listening")

# listen for incoming datagrams

while (True):

    bytes_address_pair = udp_server_socket.recvfrom(buffersize)
    message = bytes_address_pair[0]

    ip_address = bytes_address_pair[1]

    client_message = "Message from client:{}".format(message.decode("utf-8"))
    client_ip = "Client ip address:{}".format(ip_address)
    print(client_message)
    print(client_ip)

    options = "Seleccione uno de los tres canales para ver los videos: \n1. Minecraft en 1 minuto \n2. Kraft Punk \n3. Morshu Beatbox\n"

    options_bytes = str.encode(options)

    udp_server_socket.sendto(options_bytes, ip_address)

    option_selected = "{}".format(
        udp_server_socket.recvfrom(buffersize)[0].decode("utf-8"))

    if option_selected == "1":
        newAddress = address1
        fileName = nombre_video_1
        new_socket = udp_server_socket1
    elif option_selected == "2":
        newAddress = address2
        fileName = nombre_video_2
        new_socket = udp_server_socket2
    else:
        newAddress = address3
        fileName = nombre_video_3
        new_socket = udp_server_socket3

    f = open(fileName, "rb")

    #udp_server_socket.sendto(data, ip_address)
    data = f.read(buffersize)
    while data:
        if new_socket.sendto(data, ip_address):
            print("sending...")
            data = f.read(buffersize)
    f.close()
