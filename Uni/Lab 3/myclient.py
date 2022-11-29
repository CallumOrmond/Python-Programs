import socket
import sys

cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli_sock.connect((sys.argv[1], int(sys.argv[2])))




while True:
    Msg = input("Client: ")
    if Msg == "":
        Msg = " "
        
    if Msg == "EXIT":
        Msg = Msg.encode('utf-8')
        cli_sock.sendall(Msg)
        cli_sock.close()
        break
        
    Msg = Msg.encode('utf-8')
    cli_sock.sendall(Msg)
    request = cli_sock.recv(1024)
    print("Server: " + request.decode('utf-8'))


