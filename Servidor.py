#Servidor 
import socket

host = "localhost"
port = 9006
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((host,port))
servidor.listen(1)
print("Nueva conexion")

conexion, addr = servidor.accept()

while True:
    recibido = conexion.recv(1040)
    print("Cliente", recibido.decode(encoding=  "ascii", errors=  "ignore"))
    enviar = input("Servidor: ")
    conexion.send(enviar.encode(encoding=  "ascii", errors=  "ignore"))
conexion.close()
