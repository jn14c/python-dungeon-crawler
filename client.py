import socket
import sys
#client module to connect to the rpg server and play the game
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 9000)
sock.connect(server_address)
data = ""
while 1: 
	data = sock.recv(8192)
	print data
	
	if not data:
		break
	userIn = raw_input("")
	sock.send(userIn)
sock.close()
sys.exit()
