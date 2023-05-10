import socket

HOST = "192.168.1.12"  # The server's hostname or IP address
PORT = 5050  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

datastr = data.decode("utf-8").strip('\n')
print(f"Received {datastr}")