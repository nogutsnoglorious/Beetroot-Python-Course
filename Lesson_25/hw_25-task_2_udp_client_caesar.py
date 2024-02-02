import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    message = "3Hello, UDP server"
    s.sendto(message.encode(), (HOST, PORT))
    data, server = s.recvfrom(1024)
    print(f"Received encrypted response: {data.decode()} from {server}")
