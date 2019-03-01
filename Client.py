import socket

image = "" #path or name of image

HOST = '' #print there host
PORT = 60

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
sock.connect(server_address)

try:

    # open image
    myfile = open(image, 'rb')
    bytes = myfile.read()
    size = len(bytes)

    # send image size to server
    sock.sendall("SIZE %s" % size)
    answer = sock.recv(4096)

    # send image to server
    if answer == 'GOT SIZE':
        sock.sendall(bytes)

        answer = sock.recv(4096)

        if answer == 'GOT IMAGE':
            sock.sendall("Done!")

    myfile.close()

finally:
    sock.close()
