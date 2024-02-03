import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b'Hello, UDP server', (HOST, PORT))
    data, server = s.recvfrom(1024)  # Buffer size is 1024 bytes
    print(f"Received response: {data.decode()} from {server}")
