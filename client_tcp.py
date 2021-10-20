# Cliente TCP
import socket
import rsa
pub_key = 'c:\\chaves\\chavePub.txt'
arquivo = open(pub_key, 'rb')
key = arquivo.read()
arquivo.close()

pub = rsa.PublicKey.load_pkcs1(key, format='PEM')

# Endereco IP do Servidor
SERVER = '127.0.0.1'
# Porta que o Servidor esta escutando
PORT = 5002
tcp = socket.socket(socket.AF_INET,
                    socket.SOCK_STREAM)
dest = (SERVER, PORT)
tcp.connect(dest)
print('Para sair use CTRL+X\n')
msg = input()
while msg != '\x18':
    msgc = rsa.encrypt(msg.encode(), pub)
    tcp.send(msgc)
    msg = input()
tcp.close()
