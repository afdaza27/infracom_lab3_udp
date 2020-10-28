import socket
import sys
import threading
import time
from datetime import datetime
import os


def archivoLmao(nombre,  socket,  clientes):
    for i in range(clientes):
        servidorDelegado = threading.Thread(
            target=atenderCliente(nombre, socket, i))
        servidorDelegado.start()


def atenderCliente(file_name, socket, id):
    print("Atendiendo cliente "+str(id)+"...")
    st = os.stat(file_name)
    now = datetime.now()
    current_time = now.strftime("%H-%M-%S")
    log_file = open("./logs/server/log-servidor-delegado-" +
                    str(id)+"-"+current_time+".txt", "w")
    log_file.write("Se inicia el envio del archivo a las "+current_time+"\n")
    log_file.write("Se enviara el archivo "+file_name+"\n")
    f = open(file_name, "rb")

    log_file.write("El tamaño del archivo es de "+str(st.st_size)+" Bytes\n")
    data = f.read(buffersize)
    bytes_address_pair = udp_server_socket.recvfrom(buffersize)
    hash_string = str(hash(f))
    hash_bytes = str.encode(hash_string)

    message = bytes_address_pair[0]

    ip_address = bytes_address_pair[1]
    udp_server_socket.sendto(hash_bytes, ip_address)
    client_message = "Message from client:{}".format(message)
    client_ip = "Client ip address:{}".format(ip_address)
    print("message from client: " + client_message)
    print("client address: " + client_ip)
    start_time = time.time()
    n = 0

    # udp_server_socket.sendto(data, ip_address)
    while data:
        n += 1
        if udp_server_socket.sendto(data, ip_address):
            print("sending...")
            data = f.read(buffersize)
    end_time = time.time()
    log_file.write("El archivo se envio con exito en un tiempo de " +
                   str(round(end_time-start_time, 5))+" segundos\n")
    log_file.write("Total de segmentos enviados: "+str(n)+" segmentos\n")
    f.close()


localip = "0.0.0.0"

localport = 20001

buffersize = 8192
address = (localip, localport)


# create a datagram socket

udp_server_socket = socket.socket(
    family=socket.AF_INET, type=socket.SOCK_DGRAM)

# bind to address and ip

udp_server_socket.bind((localip, localport))

print("udp server up and listening")

# listen for incoming datagrams
while True:
    ejecutado = False
    while not ejecutado:
        print("-------------------------------------------------------")
        print("Bienvenido a TuServidorUDP")
        print("¿Qué deseas hacer?")
        print("1. Ver archivos disponibles")
        print("2. Enviar archivos")
        print("-------------------------------------------------------")
        risposta = int(input(""))
        if risposta == 1:
            print("1. video.mp4")
            print("2. documental.mp4")
        elif risposta == 2:
            print("¿Qué archivo desea enviar?")
            print("-------------------------------------------------------")
            print("1. video.mp4 (100MB)")
            print("2. documental.mp4 (200MB)")
            print("-------------------------------------------------------")
            archivo = input("")
            clientes = int(
                input("Ingrese la cantidad de clientes a enviar el archivo\n"))
            if archivo == "1":
                archivoLmao("video.mp4", udp_server_socket, clientes)
                ejecutado = True
            elif archivo == "2":
                archivoLmao("documental.mp4", udp_server_socket, clientes)
                ejecutado = True
        else:
            print("Ingrese un valor válido, no es tan dificil lmao")
