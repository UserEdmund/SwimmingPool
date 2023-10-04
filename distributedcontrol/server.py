import socket

def main():
    server_ip = "127.0.0.1"
    server_port = 6677

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(1)

    print("Waiting for a connection...")
    client_socket, client_address = server.accept()
    print(f"Connected to {client_address}")

    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break

        print(f"Received instruction: {data}")
        if data == "forward":
            # Code for moving forward
            print("Moving forward...")
        elif data == "backward":
            # Code for moving backward
            print("Moving backward...")
        elif data == "stop":
            # Code for stopping
            print("Stopping...")
        elif data == "patrol":
            print("Patrolling...")

    client_socket.close()
    server.close()

if __name__ == "__main__":
    main()
