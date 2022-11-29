import socket
import sys

import Functions

cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli_sock.connect((sys.argv[1], int(sys.argv[2])))

Action = sys.argv[3]

if Action in ["get","put"]:
    Action = Action.encode("utf-8")         #sends action if that action needs file the server will send the action as a request for the file
    cli_sock.send(Action)
    
    check = cli_sock.recv(1024).decode("utf-8")   #Sets chack to the action comfirmed by the server, get/put
    
    file = sys.argv[4]                            #gets the filename from the cmd input
    cli_sock.sendall(file.encode("utf-8"))        #Sends filename to the server 
          
    if check == "get":
   
        Functions.Recv_File(cli_sock, file, "Client")    #Calls the function to receive data from the server 
        
    elif check == "put":
       
        Functions.Send_File(cli_sock, file)              #Calls the function to send data to the server 
        
    
elif Action == "list":                                   
        
        for i in eval(request):                          #loops through the list of directories sent by the server               
            print(i)                                     #Eval turns the List in a string into a List
else:
    pass      
     
print("\n Now Closing Connection" , int(sys.argv[2]))    #PRINT
cli_sock.close()
   
