import socket

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"UDP Server listening on {HOST}:{PORT}")
    while True:
        data, addr = s.recvfrom(1024)
        message = data.decode()
        shift = int(message[0])
        text = message[1:]
        encrypted_message = caesar_cipher(text, shift)
        print(f"Received message: {text} with shift {shift} from {addr}")
        s.sendto(encrypted_message.encode(), addr)
