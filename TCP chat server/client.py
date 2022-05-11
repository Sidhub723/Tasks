#client side stuff

import socket
import sys
import selectors
import json


connection = False
global host         #host ip - ip of server and particular port on that server
global port 
global clientsock
global connected
host = '' # some ip address here
port = 3333
connected = False


try:
    
    clientsock = socket.socket()
    clientsock = socket.create_connection(str(host),port)    # client creates a connection with host,port of server. client does not do 'bind' but does 'connect'
    
except socket.error as txt:
    print("Oops! There was an error in socket creation :( \n")
    # can put 'do you want to try again' here

while connected == True :
    chats = clientsock.recv(1024)
    #chattxt = json.loads(chats)
    print("Messages will be displayed now : \n \n \n")
    print(chats)

    # maybe could include an option to view all old chats