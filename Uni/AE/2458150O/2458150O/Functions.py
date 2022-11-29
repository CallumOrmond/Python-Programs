import socket
import sys
import os


def Send_File(socket, filename):
    
   print("\n Get and Send ---> ", filename)      #PRINT
   
   Send = open(filename,"rb")                    #Set Send to the file that has been opened in read binary
   Send = Send.read()                            #Set Send to all the data in the file 
   #Send.close()                                  #Close file
   
   fileSize = (len(Send) / 1024)                 #Gets file size in KBs for number of loops 
   if fileSize == 0:                             #checks if the file is empty, changes value to allow empty file to be made 
        fileSize = -1
   fileSize = int(fileSize) + 1
   
   socket.send((str(fileSize)).encode("utf-8"))  #Sends file size
   
   for i in range(fileSize):                     #iterate through file sending a KB at a time 
        socket.send(Send[i * (1024):1024 + (i * (1024))])    #Send Send 
  
   print("\n Sent")                              #PRINT
   
   return
   
   
   
def Recv_File(socket, file, location):

    file = file.split("/")                       #Get the name and type of file from the file name 
    filename = file[len(file)-1]                 #Set filename to the name of the file 
    file = bytes()                               #Set file to a binary 
    
    
    fileSize = socket.recv(1024).decode("utf-8")                #receive file size for number of loops to receive a KB in 
    fileSize = int(fileSize)                                    #Set filesize to correct type for loop
         

    for i in range(fileSize):                                   #loop and receive new parts of the sent file cocatonating them 
        file = file + socket.recv(1024)
        
    
    if filename in os.listdir("C:/Users/callu/PythonPrograms/AE/" + location):     #Checks of file exists 
        print("\nFile Already Exists")                                             #stops program if file exists so there is no overriding 
        return 
    
    f = open("C:/Users/callu/PythonPrograms/AE/" + location +"/" + filename, "wb")          #create new file with name 
    f.write(file)                                                                           #write to file from information sent from server 
    print("File Write ---> " + "C:/Users/callu/PythonPrograms/AE/" + location +"/" + filename)     #PRINT
    f.close                                                                                        #Close file

    return
    
    
    
def FindConnection(PortNum):
    srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv_sock.bind(("", int(PortNum)))
    srv_sock.listen(5)
    cli_sock, cli_addr = srv_sock.accept()
    
    print("\n Connection from " + str(cli_addr)+ " has been established. \n")
    return cli_sock, cli_addr


   
   
  
