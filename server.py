import os 
import socket
import mimetypes

from app import handle

def HTTP_Server( host='127.0.0.1', port=8000):
    # HTTP Server built on TCP Server
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((host, port))
    server_sock.listen(5)

    print(f'Listening on port { port } ...\n')

    while True:
        # Wait for connection
        connection, address = server_sock.accept()
        print(f'Connected by { address[0] }/{ address[1] } \n')
        
        # Get request from client
        data = connection.recv(1024).decode()

        # Handle request
        response = handle_request(data)
        print(response, '\n')

        connection.sendall(response.encode())
        connection.close()
    
    server_sock.close()

def handle_request(request):
    method, path = parse_request(request)
    return handle(method, path)

def parse_request(data):
    # Example HTTP request: GET / HTTP/1.1  \r\n
    lines = data.split('\r\n')

    http_request = lines[0].split(' ') 
    # Get the method type (GET for example)
    method = http_request[0]

    # Get the path
    if len(http_request) > 1:
        path = http_request[1]

    return (method, path)

if __name__ == '__main__':
    HTTP_Server()

