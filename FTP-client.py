import socket
import os

HOST = 'localhost'
PORT = 6666


while True:

    try:
        request = input('>')
    except:
        break

    sock = socket.socket()

    try:
        sock.connect((HOST, PORT))
    except:
        quit()

    sock.send(request.encode())

    try:
        response = sock.recv(1024).decode()
    except:
        break

    if response == 'exit':
        break

    print(response)

    sock.close()