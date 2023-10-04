import socket

def main():
    server_ip = "192.168.0.100"
    server_port = 6677

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))
    instruction = ""

    while True:
        instruction = str(input("Enter instruction (forward/backward/stop): "))
        client.send(instruction.encode())

        if instruction == "exit":
            break

    client.close()

if __name__ == "__main__":
    main()
