import socket

HOST = '127.0.0.1'
PORT = 65432      

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"UDP Server listening on {HOST}:{PORT}")
    while True:
        data, addr = s.recvfrom(1024)
        print(f"Received message: {data.decode()} from {addr}")
        if data:
            s.sendto(data.upper(), addr)