import socket
import multiprocessing

def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            client_socket.send(data)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

def main():
    host = "127.0.0.1"  # Host IP address
    port = 12345       # Port to listen on

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Listening on {host}:{port}")

    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")
            
            # Create a new process to handle the client
            client_process = multiprocessing.Process(target=handle_client, args=(client_socket,))
            client_process.start()
    except KeyboardInterrupt:
        print("Server terminated by user.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()