import socket
import threading

# Client configuration
HOST = '127.0.0.1'  # Server's IP address
PORT = 12345

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            print(message)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            client_socket.close()
            break

def send_messages():
    while True:
        message = input()
        client_socket.send(message.encode("utf-8"))

def main():
    print("Connected to the chat server.")
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages)
    send_thread.start()

if __name__ == "__main__":
    main()
