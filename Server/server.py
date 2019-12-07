#Welcome to my server (file sender) program
#Simply call this program from the command line and supply the server's port as argument
#Your current directory may need to be the folder this program is inside of in order for it to be able to read files

import socket
import sys

port = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', port))
s.listen(1)
print "Server hosting on port:", port

while True:
    client, address = s.accept()
    print address, "Connected"

    filename = client.recv(1024)
    print "QUERY:", filename

    try:
        f = open(filename)
        data = f.read()
        print "sending file:", filename
        client.send(data)
        client.close()
    except:
        print "invalid filename supplied"
        client.send("__err__")
        client.close()

    print "done"
