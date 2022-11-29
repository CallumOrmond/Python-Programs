import socket
import sys

srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv_sock.bind(("", int(sys.argv[1])))
srv_sock.listen(5)
cli_sock, cli_addr = srv_sock.accept()

print("\n Connection from " + str(cli_addr)+ " has been established. \n")

while True:
  
   request = cli_sock.recv(8)
   
   if request.decode('utf-8') == "EXIT":
        cli_sock.close()
        srv_sock.listen(5)
        cli_sock, cli_addr = srv_sock.accept()
        print("\n Connection from " + str(cli_addr)+ " has been established. \n")
        
        request = cli_sock.recv(8)
        print("Client: " + request.decode('utf-8'))
   else:
        print("Client: " + request.decode('utf-8'))
    
    
   Msg = input("Server: ")
   if Msg == "":
        Msg = " "
   cli_sock.sendall(Msg.encode('utf-8'))
   
   
   