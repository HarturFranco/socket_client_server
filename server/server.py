import socket

class Server:
    def __init__(self):
        self._ip = "192.168.1.13" # Definindo o ip do servidor
        self._port = 2022 # Definindo a porta a ser utilizada pelo servidor
        self._bufferSize = 1024 # Definindo o tamanho do buffer
        self._address = (self._ip, self._ip) # Definindo endereço do server -> tupla (ip, porta)
    
    def listen(self):
        # criando socket 
        udpSSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # vinculando ao endereco
        udpSSocket.bind(self._address)
        
        # "escutando" por mensagens
        while(True):
            usr_message, usr_address = udpSSocket.recvfrom(self._bufferSize)
            
            # Exibe a mensagem recebida
            print(f'Client Message: {usr_message}\nClient IP: {usr_address}')
            
            # Manda para o cliente a mensagem recebida
            udpSSocket.sendto(usr_message, usr_address)
        
        

if __name__  == "__main__":
    udp_server = Server()
    udp_server.listen()
