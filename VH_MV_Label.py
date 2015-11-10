#!/usr/bin/env python

import socket
import sys
import time

# Establish TCP/IP sockets
#vcs --> Switcher
#mv --> Multiviewer
sockvcs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockmv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect sockets with devices
server_address = ('192.168.1.60', 9990)
sockvcs.connect(server_address)
time.sleep(0.4)
data = sockvcs.recv(8888)
server_address = ('192.168.1.61', 9990)
sockmv.connect(server_address)

#receive labels
sockvcs.send("input labels:\n\n")
time.sleep(0.1)
ilabels = sockvcs.recv(4096)
ilabels = ilabels.split('\n')

#receive labels
sockvcs.send("output labels:\n\n")
time.sleep(0.1)
olabels = sockvcs.recv(4096)
olabels = olabels.split('\n')

#parse outputrouting
sockvcs.send("video output routing:\n\n")
time.sleep(0.1)
outrouting = sockvcs.recv(4096)
outrouting = outrouting.split('\n')

#delete first rows
i = 0
while i <> 3:
    a = outrouting.pop(0)
    i += 1

#define number of channels - multiviewer
x = 16

#Display output routing
i = 0

while i <> x:
    ausgabe = outrouting[i].split(' ')
    outputinteger = int(ausgabe[0])
    output = olabels[int(ausgabe[0])+3][2:]
    input = ilabels[int(ausgabe[1])+3][2:]
    input = input.lstrip(' ')
    i += 1
    print str("INPUT LABELS:\n" + str(outputinteger) + " " + str(output)[3:] + " | " + str(input) + "\n\n")
    sockmv.send(str("INPUT LABELS:\n" + str(outputinteger) + " " + str(output)[3:] + " | " + str(input) + "\n\n"))

#wait for changings in Output routing
while 1:
    switch = sockvcs.recv(4096)
    switch = switch.split("\n")
    time.sleep(0.1)
    if switch[0] == "VIDEO OUTPUT ROUTING:":
        ausgabe = switch[1].split(' ')
        outputinteger = int(ausgabe[0])
        output = olabels[int(ausgabe[0])+3][2:]
        input = ilabels[int(ausgabe[1])+3][2:]
        input = input.lstrip(' ')
        print str("INPUT LABELS:\n" + str(outputinteger) + " " + str(output)[3:] + " | " + str(input) + "\n\n")
        sockmv.send(str("INPUT LABELS:\n" + str(outputinteger) + " " + str(output)[3:] + " | " + str(input) + "\n\n"))
        time.sleep(0.1)

print 'Programm beendet.'
sockvcs.close()
