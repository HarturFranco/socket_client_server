import socket
import time
import statistics

class Client:

    def __init__(self):
        self._host_server = "192.168.1.13" ## Definindo o ip do servidor ao qual irá se comunicar
        self._port = 2022 ## Definindo a porta do servidor ao qual irá se comunicar
        self._time_sleep = 0.25 ## Definindo o tempo de delay para cada envio de mensagem ao servidor
        self._transport_protocol = socket.SOCK_DGRAM ## Definindo o protocolo UDP para a camada de transporte
        self._net_protocol = socket.AF_INET ## Definindo o protocolo IP para a camada de rede
        
    def send_msg_UDP(self, qtd_msg):
        qtd_error = 0 ## Contador de pacotes perdidos
        list_time = [] ## Lista com os tempos dos pacotes que foram entregues com sucesso
        with socket.socket(self._net_protocol, self._transport_protocol) as udp_packet: ## Criando o socket com os protocolos IP/UDP
            udp_packet.settimeout(self._time_sleep) ## Setando o tempo limite de espera
            for i in range(qtd_msg):
                start = time.time() ## Pegando o tempo de inicio do envio da mensagem
                udp_packet.sendto(str.encode(str(i)), (self._host_server, self._port)) ## Enviando a mensagem para o servidor
                try:
                    response = udp_packet.recvfrom(1024) ## Recebendo a mensagem de resposta do servidor
                except: ## Para caso não receba a mensagem de resposta do servidor
                    qtd_error += 1 ## Adiciona um ao contador de pacotes perdidos
                else: ## Para caso rece a mensagem de resposta do servidor
                    list_time.append((time.time() - start) * 1000) ## Calcula tempo gasto para envio da mensagem e adiciona na lista
                time.sleep(1) ## Delay entre as mensagens
            ## Calculo das estatisticas
            print("Estatistica:")
            print("Pacotes totais: " + str(qtd_msg))
            print("Pacotes recebidos: " + str(len(list_time)) + " - " + str((len(list_time) / qtd_msg) * 100) + "%")
            print("Pacotes perdidos: " + str(qtd_error) + " - " + str((qtd_error / qtd_msg) * 100) + "%")
            print("Tempo máximo: " + str(max(list_time)) + " ms")
            print("Tempo mínimo: " + str(min(list_time)) + " ms")
            print("Tempo médio: " + str(statistics.mean(list_time)) + " ms")
            udp_packet.close() ## Fecha o socket

if __name__ == '__main__':
    cliente = Client()
    cliente.send_msg_UDP(20) ## Chama a função para enviar 20 mensagens para o servidor

