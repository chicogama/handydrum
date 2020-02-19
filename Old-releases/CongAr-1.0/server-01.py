#
import socket


def server_socket():
    HOST = '192.168.1.102'  # Endereco IP do Servidor
    PORT = 5050  # Porta que o Servidor esta
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    orig = (HOST, PORT)
    udp.bind(orig)
    while True:
        msg, cliente = udp.recvfrom(1024)
        print(msg)
        # funcao de coleta de dados
        #play_midi( msg)
    udp.close()


server_socket()

# def play_midi( msg ):
#    return 0
