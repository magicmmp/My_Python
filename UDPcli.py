import socket 
HOST_IP="127.0.0.1" 
HOST_PORT = 54831
HOST_PORT_RECEIVE = 58927
DEST_IP_ADDRESS = "127.0.0.1"
DEST_PORT_NO = 58913
BUFSIZE = 4096
buffer_to_send='I am client'
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiveSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSock.bind((HOST_IP, HOST_PORT))
receiveSock.bind((HOST_IP, HOST_PORT_RECEIVE))
clientSock.sendto(buffer_to_send, (DEST_IP_ADDRESS, DEST_PORT_NO))
print 'send:',buffer_to_send
command_echo = receiveSock.recvfrom(BUFSIZE)
print 'receive:',command_echo
clientSock.close() 
receiveSock.close()
