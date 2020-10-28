import socket
import threading
from datetime import datetime
import os
import time


def run_cliente(id):
    now = datetime.now()
    current_time = now.strftime("%H-%M-%S")
    log_file = open("./logs/client/log-client-" +
                    str(id)+"-"+current_time+".txt", "w")
    log_file.write("Se inicia la descarga del archivo a las " +
                   current_time+"\n")
    print("running client "+str(id))
    message_from_client = "yo"
    bytes_to_send = str.encode(message_from_client)
    server_address_port = ("127.0.0.1", 20001)
    buffer_size = 8192
    destination_file_path = "./vids/recieve-"+str(id)+"-"+current_time+".mp4"
    f = open(destination_file_path, "wb")
    log_file.write("Se guardara el archivo en "+destination_file_path+"\n")
    # create a UDP socket at client side
    udp_client_socket = socket.socket(
        family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # udp_client_socket.bind(server_address_port)
    # send to server using created udp socket
    udp_client_socket.sendto(bytes_to_send, server_address_port)
    hash_sent, addr = udp_client_socket.recvfrom(buffer_size)
    data, addr = udp_client_socket.recvfrom(buffer_size)
    start_time = time.time()
    n = 0
    try:
        while data:
            n += 1
            f.write(data)
            udp_client_socket.settimeout(2)
            data, addr = udp_client_socket.recvfrom(buffer_size)
    except:
        if str(hash(f)) != hash_sent.decode("utf-8"):
            log_file.write("El hash del archivo enviado ("+hash_sent.decode("utf-8") +
                           ") no corresponde al del archivo descargado ("+str(hash(f))+"). Por lo tanto, el archivo recibido esta incompleto.\n")
        else:
            log_file.write("El archivo fue descargado con integridad.\n")
        f.close()
        udp_client_socket.close()
        print("file downloaded")
        end_time = time.time()
        st = os.stat(destination_file_path)
        log_file.write("El tamaño del archivo es de " +
                       str(st.st_size)+" Bytes\n")
        log_file.write("El archivo se descargo con exito en un tiempo de " +
                       str(round(end_time-start_time, 5))+" segundos\n")
        log_file.write("Total de segmentos descargados: " +
                       str(n)+" segmentos\n")


clientes = int(input("Ingrese la cantidad de clientes:\n"))
for i in range(clientes):
    cliente = threading.Thread(target=run_cliente(i))
    cliente.start()
