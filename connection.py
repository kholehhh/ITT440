import socket

SERVER_IP = 'izani.synology.me'
SERVER_PORT = 8443
BUFFER_SIZE = 1024

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        student_id = "2021619528"
        client_socket.send(student_id.encode())
        response = client_socket.recv(BUFFER_SIZE).decode()
        print("Server Response:", response)

    except ConnectionRefusedError:
        print("Connection refused. Please check the server address and port.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
