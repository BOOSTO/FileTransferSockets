#Welcome to my client (file reciever) program
#Simply call this program from the command line and supply the server's port as argument

import socket
import sys
import os

server_port = int(sys.argv[1])

print "server_port:", server_port

filename = raw_input("What file shall I retrieve: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', server_port))
s.send(filename)

packet = ""
f = open(filename, "a")
while True:
    packet = s.recv(1024)
    if "__err__" in packet:
        print "invalid filename"
        os.remove(filename)
        break
    if not packet:
        print "complete"
        break
    f.write(packet)
f.close()
s.close()
