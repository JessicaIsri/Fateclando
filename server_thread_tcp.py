# Servidor TCP
import socket
import rsa
from threading import Thread

pri_key = 'c:\\chaves\\chavePri.txt'
arquivo = open(pri_key, 'rb')
key = arquivo.read()
arquivo.close()
pri = rsa.PrivateKey.load_pkcs1(key, format='PEM')


def conexao(con, cli):
    while True:
        msg = con.recv(1024)
        if not msg: break
        decode_msg = rsa.decrypt(msg, pri)
        print("Without Decrypt: \n", msg)
        print("Decode message: \n", decode_msg)
    print('Finalizando conexao do cliente', cli)
    con.close()


# Endereco IP do Servidor
HOST = ''
# Porta que o Servidor vai escutar
PORT = 5002
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print('Concetado por ', cliente)
    t = Thread(target=conexao, args=(con, cliente,))
    t.start()
