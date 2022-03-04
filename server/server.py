import socket
from socketserver import UDPServer

ip = "192.168.1.13"
port = 2022

bufferSize = 1024

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orign = (ip, port)
udp.bind(orign)

while(True):
    message, address = udp.recvfrom(bufferSize)
    
    print(f'Client Message: {message}\nClient IP: {address}')
    
    # Manda para o cliente a mensagem recebida
    udp.sendto(message, address)