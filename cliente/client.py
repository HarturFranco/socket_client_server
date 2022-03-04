import socket
import time

class Client:

    def __init__(self):
        self._host_server = "192.168.1.13" ## Definindo o ip do servidor ao qual irá se comunicar
        self._port = 2022 ## Definindo a porta do servidor ao qual irá se comunicar
        self._time_sleep = 0.25 ## Definindo o tempo de delay para cada envio de mensage ao servidor
        self._transport_protocol = socket.SOCK_DGRAM
        self._net_protocol = socket.AF_INET
        
    def send_msg_UDP(self, qtd_msg):
        list_error = []
        list_correct = []
        list_time = []
        with socket.socket(self._net_protocol, self._transport_protocol) as udp_packet:
            udp_packet.settimeout(self._time_sleep)
            for i in range(qtd_msg):
                start = time.time()
                udp_packet.sendto(str.encode(str(i)), (self._host_server, self._port))
                try:
                    response = udp_packet.recvfrom(1024)
                except:
                    list_error.append(response[0])
                else:
                    list_time.append((time.time() - start) * 1000)
                    list_correct.append(response[0])
                time.sleep(1)
            print("Estatistica:")
            print("Pacotes totais: " + str(len(list_error) + len(list_correct)))
            print("Pacotes recebidos: " + str(len(list_correct)) + " - " + str((len(list_correct) / (len(list_error) + len(list_correct))) * 100) + "%")
            print("Pacotes perdidos: " + str(len(list_error)) + " - " + str((len(list_error) / (len(list_error) + len(list_correct))) * 100) + "%")
            print("Tempo máximo: " + str(max(list_time)) + " ms")
            print("Tempo mínimo: " + str(min(list_time)) + " ms")
            print("Tempo médio: " + str(sum(list_time)/len(list_time)) + " ms")
            udp_packet.close()

if __name__ == '__main__':
    cliente = Client()
    cliente.send_msg_UDP(20)

