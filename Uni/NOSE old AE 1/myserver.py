import socket
import sys
import os

import Functions


while True:                                   

   cli_sock, cli_addr = Functions.FindConnection(sys.argv[1])      #funtion to listen for and to connect to new clients 
   
   request = cli_sock.recv(1024).decode('utf-8')                   #receives the Actions requested by the client
   
   if request == "get":                                        
       
       cli_sock.sendall(request.encode('utf-8'))                   #Send request for the filename from the Client
       filename = cli_sock.recv(1024).decode('utf-8')              #Gets filename
       
       Functions.Send_File(cli_sock, filename)                     #Calls function to send files to the client 
          
          
   elif request == "put":  
       cli_sock.sendall(request.encode('utf-8'))                   #Send request for the filename from the Client
       filename = cli_sock.recv(1024).decode("utf-8")              #Gets filename
       
       Functions.Recv_File(cli_sock, filename , "Server")          #Calls function to receive file from client
       
       
   elif request == "list":
        cli_sock.send(str(os.listdir()).encode('utf-8'))           #Sends the list of directories as a string 
   

   
   