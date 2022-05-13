####################################client side stuff#################################

from concurrent.futures import thread
import socket
import threading
import sys
#import selectors
#import json
import time



connection = False
global host         
global port 
global clientsock
global connected
host = '127.0.0.1'  # connecting to localhost
port = 12345
connected = False

def connector():
    global host,port,clientsock,connected
    try:
        
        clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # AF_INET ensures that the communication occurs through the internet and SOCK_STREAM ensures that is happens through TCP
        clientsock = socket.create_connection((host,port))    # client creates a connection with host,port of server. client does not do 'bind' but does 'connect' with a port on the host
        print("You are being connected...")
        connected = True
    except socket.error as txt:
        print("Oops! There was an error in socket creation :( \n")
        # can put 'do you want to try again' here

    while connected == True :
        try:
            chats = clientsock.recv(1024).decode("utf-8")       #receiving data from the server through the socket
            #chattxt = json.loads(chats)
            if "Welcome to the chat" in chats :
                print("Messages will be displayed now : \n")
            print(chats)
        except:
            clientsock.close()
            break
            #print("Server has closed \n Will close in 5 seconds..")
            #time.sleep(5)
            #sys.exit()
        
def messaging():
    global clientsock
    global connected
    while True:
        try:
            if connected == True:
                texts = input("")
                if "/leave" in texts:
                    clientsock.close()
                    time.sleep(3)
                    sys.exit()
                clientsock.send(texts.encode("utf-8"))
        except :
            print("Exiting in 5 seconds")
            time.sleep(5)
            sys.exit()


connectorThread = threading.Thread(target = connector).start()      #creating and starting the thread for the connection function so that multiple clients(and sockets) can be created on the same system
messagingThread = threading.Thread(target = messaging).start()      #creating and starting the thread for the messaging function to continuously be able to send and receive data





# maybe could include an option to view all old chats
