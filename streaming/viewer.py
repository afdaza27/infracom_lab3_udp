import socket
import viewertest
import vlc

message_from_client = "yo"

bytes_to_send = str.encode(message_from_client)

server_address_port = ("127.0.0.1", 20001)

buffer_size = 1024

destination_file_name = "temp.mp4"

f = open(destination_file_name, 'w')
f.close()

f = open(destination_file_name, "wb")

# create a UDP socket at client side

udp_client_socket = socket.socket(
    family=socket.AF_INET, type=socket.SOCK_DGRAM)
# udp_client_socket.bind(server_address_port)


# send to server using created udp socket

udp_client_socket.sendto(bytes_to_send, server_address_port)

opcion = input("{}".format(
    udp_client_socket.recvfrom(buffer_size)[0].decode("utf-8")))

udp_client_socket.sendto(str.encode(opcion), server_address_port)

data, addr = udp_client_socket.recvfrom(buffer_size)


try:
    while data:
        f.write(data)
        udp_client_socket.settimeout(2)
        data, addr = udp_client_socket.recvfrom(buffer_size)
except:
    f.close()
    udp_client_socket.close()
    Instance = vlc.Instance("--fullscreen")
    player = Instance.media_player_new()
    Media = Instance.media_new(destination_file_name)
    Media.get_mrl()
    player.set_media(Media)
    player.play()

    option = input("Ingrese stop para detener el video\n")
    if(option == "stop"):
        player.stop()
