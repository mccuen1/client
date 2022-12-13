import socket

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER_PORT = 8081
SERVER_IP = '10.103.65.12'  # Nates's IP Address

def send_message(msg, client_socket):
    message = msg.encode(FORMAT)

    # calc length
    msg_length = len(message) 
    # encode the length
    msg_length = str(msg_length).encode(FORMAT)
    # pad with white spaces
    msg_length += b' ' * (HEADER - len(msg_length))

    client_socket.send(msg_length)
    client_socket.send(message)

def start_client():
    SERVER_ADDR = (SERVER_IP, SERVER_PORT)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect(SERVER_ADDR)
    msg = input('Enter the message to be sent to the server (Type quit to exit): ')
    while msg != 'quit':
        send_message(msg, client_socket)
        msg = input('Enter a message or type quit to exit: ')
    send_message(DISCONNECT_MESSAGE, client_socket)
    client_socket.close()
    print("Sending Disconnect request to the server.")

start_client()