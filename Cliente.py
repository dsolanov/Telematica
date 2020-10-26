#Cliente
import socket

host = "localhost"
port = 9006
Cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Cliente.connect((host, port))
print ("Nueva conexion!")

while True:
    enviar = input("Cliente: ")
    Cliente.send(enviar.encode(encoding=  "ascii", errors=  "ignore"))
    recibido = Cliente.recv(1040)
    print("Servidor", recibido.decode(encoding= "ascii", errors= "ignore"))
Cliente.close()