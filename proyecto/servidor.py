import socket

dir_servidor =('localhost',10000)
buffer = 1024


sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.bind(dir_servidor)

print("[{}]iniciando servidor")

while True:

    data, ip = sock.recvfrom(buffer)


    print("{}:{}".format(ip,data.decode()))

