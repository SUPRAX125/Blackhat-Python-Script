#!/usr/bin/env python
import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#server membuat listed
server.bind((bind_ip, bind_port))

#server start listed
server.listen(2)

print("[*] Listening on %s: %d" % (bind_ip, bind_port))

#client-handling thread
def handle_client(client_socket):

    #cetak apa yg dikirim client
    request = client_socket.recv(1024)

    print("[*] Received: %s \n" % (request))

    #kirim kembali packet
    client_socket.send("ACK!".encode())

    client_socket.close()

while True:
    client, addr = server.accept()

    print("[*] Accepted connection from: %s %d" % (addr[0], addr[1]))

    #spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(client, ))
    client_handler.start()

#ini kudu jalanin tcp-client/udp-client dulu