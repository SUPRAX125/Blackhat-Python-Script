#!/usr/bin/env python

import socket
import sys

#buat target langsung di terminal
target_host = sys.argv[1]
target_port = int(sys.argv[2])
#target_host = "www.detik.com"
#target_port = 80

#buat socket object dari kelas socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET itu artinya kita pake IPv4 Standar, SOCK_STREAM itu artinya pake tcp client

#konek client ke server
client.connect((target_host,target_port)) #TCP perlu dikonekin dulu

#send data ke target
#client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".encode()) #targetnya udh dikonekin
client.send("berisik".encode())

#membuat response
response = client.recv(2048)

print(response)