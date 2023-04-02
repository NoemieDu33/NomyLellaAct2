import socket
import cam_imgReturn

IP = '10.3.141.1'
PORT = 5050

# -------- serveur TCP 
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP,PORT))
server.listen(5)
conn = False
while not conn:
	conn, addr = server.accept()
print(f"New connection: {addr}")
while True:
	data = conn.recv(1024)
	print("received message : %s" %data)
	print(data, type(data))	
	if data:
		break	
conn.close()
print("fin serveur")
# -------- traitement de l'image
output = cam_img.letterimg()
if not output.strip():
	output="Rien"
# ------- client TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
print(f"Connected to host")
n = client.send(output)
if n != len(output):
        print("Error sending output")
client.close()
