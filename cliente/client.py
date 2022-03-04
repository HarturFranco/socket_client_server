import socket

class Client:

    def __init__(self):
        self._host_server = "192.168.1.13" ## Definindo o ip do servidor ao qual irá se comunicar
        self._port = "2022" ## Definindo a porta do servidor ao qual irá se comunicar
        self._time_sleep = 0.5 ## Definindo o tempo de delay para cada envio de mensage ao servidor
        self._transport_protocol = socket.SOCK_DGRAM
        self._net_protocol = socket.AF_INET
        
    def send_msg_UDP(self, qtd_msg):
        with socket.socket(self._net_protocol, self._transport_protocol) as udp_packet:
            udp_packet.settimeout(self._time_sleep)
            for i in range(qtd_msg):
                udp_packet.sendto(str.encode(str(i)), (self._host_server, self._port))
                response = udp_packet.recvfrom(1024)
                print("Mensagem de envio foi: " + str(i) + "\nPorém codificada assim: " + str.encode(str(i)))
                print("Mensagem de resposta do servidor foi: " + str(response))

if __name__ == '__main__':
    cliente = Client()
    cliente.send_msg_UDP(5)

