import socket

dir_servidor =('localhost',10000)
print ("cliente esta iniciando")

while True:
        print("Escribe tu mensaje (para salir teclea enter)")
        mensaje= input()


        if not mensaje: break

        sock= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sock.sendto(mensaje.encode(),(dir_servidor))
        