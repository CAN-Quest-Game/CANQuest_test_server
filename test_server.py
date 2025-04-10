import socket
import threading
import keyboard  # Import the keyboard module

# Server address
IP = ''  # input your ip address here, or use '' for localhost
PORT = 8080



# Function to handle receiving messages from the client
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message or message.lower() == 'exit':
                print("Connection closed by client.")
                break
            print(f"Received from client: {message}")
        except ConnectionResetError:
            print("Connection reset by client.")
            break
    client_socket.close()

# Function to handle sending messages to the client
def send_messages(client_socket):
    while True:
        message_to_send = input("Enter message to send: ")
        if message_to_send.lower() == 'exit':
            print("Closing connection...")
            client_socket.sendall('exit'.encode('utf-8'))
            client_socket.close()
            break
        client_socket.sendall(message_to_send.encode('utf-8'))

# Main server function
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(1)
    print(f"Server listening on {IP}:{PORT}...")
    
     # Listen for 'k' key press to kill the server
    keyboard.add_hotkey('k', shutdown_server, args=(server_socket,))

    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    # Start threads for sending and receiving messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    
    receive_thread.start()
    send_thread.start()

    # Wait for both threads to finish
    receive_thread.join()
    send_thread.join()

    server_socket.close()
    
# Function to handle server shutdown
def shutdown_server(server_socket):
    print("Shutting down server...")
    server_socket.close()
    exit(0)


if __name__ == "__main__":
    print("Starting server...")
    start_server()