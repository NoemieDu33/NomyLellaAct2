import socket

HOST = "10.3.141.100"  # The server's hostname or IP address
PORT = 5050  # The port used by the server
def camembert():
    msg = ""
    with open("detect.txt","r") as f:
        msg = f.readlines()[0].strip().strip('\n').upper()
    print(msg)
    bmsg=msg.encode('utf-8')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(bmsg)
        data = s.recv(1024)

    datastr = data.decode("utf-8").strip('\n')
    print(f"Received {datastr}")
