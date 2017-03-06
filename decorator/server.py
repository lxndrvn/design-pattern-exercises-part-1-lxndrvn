import socket
from logsocket import *
from obscene_filter_socket import *

def respond(client):
    response = input("Enter a value: ")
    client.send(bytes(response, 'utf8'))
    client.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost',2401))
server.listen(1)

try:
    while True:
        client, addr = server.accept()
        respond(ObsceneFilterSocket(client))
finally:
    server.close()
