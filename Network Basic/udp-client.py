#!/usr/bin/env python

import socket, sys

target_host = sys.argv[1]
target_port = int(sys.argv[2])

#buat objek untuk kelas socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#ngirim data
client.sendto("AAABBBCCC".encode(), (target_host, target_port))

#response
data, addr = client.recvfrom(4096)

#print("for data",data)
#print("for addr", addr)
print(data)

#karena koneksinya UDP jadi gak pake .connect()
#karena dia connectionless