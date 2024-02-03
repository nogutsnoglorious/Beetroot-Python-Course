import socket

def main():
    host = "127.0.0.1" 
    port = 12345    

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((host, port))
        
        while True:
            message = input("Enter a message (or 'quit' to exit): ")
            
            if message.lower() == 'quit':
                break
            
            client_socket.send(message.encode())
            
            response = client_socket.recv(1024)
            print(f"Server response: {response.decode()}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
