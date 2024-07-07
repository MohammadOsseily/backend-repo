from dotenv import load_dotenv
import os
import socket


load_dotenv()
SERVER_IP_ADDRESS = os.getenv('SERVER_IP_ADDRESS', '127.0.0.1')
SERVER_PORT = int(os.getenv('SERVER_PORT', 5000))

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP_ADDRESS, SERVER_PORT))
    server_socket.listen(5)
    print(f"Server listening on {SERVER_IP_ADDRESS}:{SERVER_PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        client_socket.sendall(b"Hello from the server!")
        client_socket.close()

if __name__ == "__main__":
    main()
