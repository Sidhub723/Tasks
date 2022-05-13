###############################Server ##########################

global coldict 
#colour data as well as bold, italics etc! It is a Ctype terminal formatting code

coldict = {
'CEND'      : '\33[0m',
'CBOLD'     : '\33[1m',
'CITALIC'   : '\33[3m',
'CURL'      : '\33[4m',
'CSTRIKETHROUGH' : '\33[9m',
'CBLINK'    : '\33[5m',
'CBLINK2'   : '\33[6m',
'CSELECTED' : '\33[7m',
'CBLACK'  : '\33[30m',
'CRED'    : '\33[31m',
'CGREEN'  : '\33[32m',
'CYELLOW' : '\33[33m',
'CBLUE'   : '\33[34m',
'CVIOLET' : '\33[35m',
'CBEIGE'  : '\33[36m',
'CWHITE'  : '\33[37m',
'CBLACKBG'  : '\33[40m',
'CREDBG'    : '\33[41m',
'CGREENBG'  : '\33[42m',
'CYELLOWBG' : '\33[43m',
'CBLUEBG'   : '\33[44m',
'CVIOLETBG' : '\33[45m',
'CBEIGEBG'  : '\33[46m',
'CWHITEBG'  : '\33[47m',
'CGREY'    : '\33[90m',
'CRED2'    : '\33[91m',
'CGREEN2'  : '\33[92m',
'CYELLOW2' : '\33[93m',
'CBLUE2'   : '\33[94m',
'CVIOLET2' : '\33[95m',
'CBEIGE2'  : '\33[96m',
'CWHITE2'  : '\33[97m',
'CGREYBG'    : '\33[100m',
'CREDBG2'    : '\33[101m',
'CGREENBG2'  : '\33[102m',
'CYELLOWBG2' : '\33[103m',
'CBLUEBG2'   : '\33[104m',
'CVIOLETBG2' : '\33[105m',
'CBEIGEBG2'  : '\33[106m',
'CWHITEBG2'  : '\33[107m' }

from multiprocessing.connection import Client
import socket
import sys
import time
import threading




class server():

    global serverip
    global serverport
    global count
    global locations
    global serversock
    serverip = "127.0.0.1" # some server ip address
    serverport = 12345
    count = 0               #counts number of active users
    locations = []          #stores the location of the user as (ip,port)

    def __init__(self):
        self.clients = []
        #self.locations = []


    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      #AF_INET ensures the sockets communicate through the internet and SOCK_STREAM ensures that the communication is according to the TCP protocol
    serversock.bind((serverip,serverport))   # BINDING the socket to the ip of the server itself and a port on it so that all incoming connection recieved by the socket are redirected to the server itself
    serversock.listen(30)               # the socket is now listening on a port on the ip of the server
    print("Server is now active and listening!")

    
    def initialiser(self):

        global serverip
        global serverport
        global count
        global locations
        global serversock

        #try:
        while True:
            clisock,addr = serversock.accept()       # accepting any socket connections while the server socket is listening
            a = input("A connection has arrived from "+ str(addr[0])+ " via port "+str(addr[1]) +" \n Do you want to accept it?? Y/N")
            if (a == 'N') | (a == 'n') :
                clisock.send("Sorry, your connection has been declined :( ".encode("utf-8"))
                clisock.close()                     #closing the clients connection if declined
                break

            elif (a =='y') | (a == 'Y') :

                count += 1
                print("Client has joined. IP : "+str(addr[0]) + " , and via port : "+ str(addr[1])+ " at time : "+time.strftime("%a, %d %b %Y %H:%M:%S" + " . \n")) # visible to the person running server
                print(str(count) + " clients currently online")
                clisock.send('Welcome to the chat server! You should now be able to view messages from others, as well as post your own \n If you want to leave the chatroom then type /leave \n Enjoy your stay!'.encode("utf-8"))
                self.broadcaster("User has joined room! Total online users are "+str(count))  # message broadcasted to all other active users
                self.clients.append(clisock)
                #self.locations.append([addr[0],addr[1],count])
                locations.append([addr[0],addr[1],count])
                thread = threading.Thread(target = self.clienthandler, args = (clisock,)).start()       #creating and starting the thread to multithread the clienthandler so that multiple clients can send in data through the socket
                
                       
            else :
                print("Wrong input :(")

        '''except socket.error as txt:
            print("Could not start server thread :(")
            time.sleep(4)
            sys.exit()  '''





    def broadcaster(self,message):
        for c in self.clients:                  #the broadcaster simply sends the message sent by one client to each and every client in the client array
            try:
                c.send(message.encode("utf-8"))

            except socket.error as txt :
                c.send('The message failed to send :( \n Try to send it again or close and reopen your connection!'.encode("utf-8"))






    def clienthandler(self,ClientsSocket):                  #clisock is sent as ClientsSocket
        
        global serverip
        global serverport
        global count
        global locations
        
        while True :
        
            try:
                data = ClientsSocket.recv(1024).decode("utf-8")
            except Exception as txt :
                print("Oops, looks like the client has left!")
                count -= 1
                print(str(count)+ " clients remaining")
                raise SystemExit(txt)

            #if not data :
            #    break
            #print("clienthadnler had recieved data")

            if str(data) == '/leave':                           # /leave is the keyword for the client to close his connection
                index = self.clients.index(ClientsSocket)
                details = locations[index]                      # array containing ip and port
                ClientsSocket.send("You will be removed in 5 seconds...".encode("utf-8"))
                time.sleep(5)

                    
            
            #formatting the data here as per the task!
            coltype = ''
            if "/colour" in str(data):      #changing colour
                ind = str(data).index('/')
                ind = ind + 8 # index of thr first letter of the actual colour
                end = str(data).index(' ',ind)  # /colour 
                #print(ind)
                #print(end)
                colo = str(data)[ind:end].upper()
                
                for keys in coldict :
                    if colo in keys:
                        #colo = str(colo)
                        coltype = coldict[str('C'+colo)]
                        data = coldict[str('C'+colo)] + str(data) + coldict['CEND']     #changing the colour

                '''print(coltype)
                coltype = coltype[1:]
                coltype = '\33' + coltype
                print(coltype) '''
                data = coldict[coltype] + str(data) + coldict['CEND']

            if "/leave" in str(data):
                #self.broadcaster("A user has left")
                #self.locations.remove(self.clients.index(ClientsSocket))
                self.broadcaster("User from ip: "+ str(locations[index][0]) +" and port : " + str(locations[index][2]) + " has left")
                del self.locations[self.clients.index(ClientsSocket)]       
                self.clients.remove(ClientsSocket)
                
                count -= 1
                ClientsSocket.close()

            if "/private" in str(data):
                pass
                #open a new socket between requester and requested client?
                
            if str(data).count("**") == 2 : #wont work if there are multiple such bold text aesterisks 
                start = str(data).index("**")
                end = str(data).index("**",start+1)
                #data = coldict['CBOLD'] + str(data) + coldict['CEND']
                data = str(data)[0:start] + coldict['CBOLD'] + str(data)[start:end+1] + coldict['CEND']

            if str(data).count("__") == 2:
                start = str(data).index("__")
                end = str(data).index("__",start+1)
                #data = coldict['CITALIC'] + str(data) + coldict['CEND']
                data = str(data)[0:start] + coldict['CITALIC'] + str(data)[start:end+1] + coldict['CEND']

            if str(data).count("~~") == 2:
                start = str(data).index("~~")
                end = str(data).index("~~",start+1)
                #data = coldict['CSTRIKETHROUGH'] + str(data)
                data = str(data)[0:start] + coldict['CSTRIKETHROUGH'] + str(data)[start:end+1] + coldict['CEND']
        
            '''except:

                index = self.clients.index(ClientsSocket)
                self.broadcaster("User from ip: "+ str(locations[index][0]) +" and port : " + str(locations[index][2]) + " has left")
                self.clients.remove(ClientsSocket)
                del locations[index]
                count -= 1
                ClientsSocket.close()
                #self.broadcaster("A user has left the chat")'''



            for client in self.clients:
                client.send(data.encode("utf-8"))

        '''self.clients.remove(ClientsSocket) # removes from list of active clients
        count -= 1
        ClientsSocket.close() # also closes the clients connection'''


if __name__ == "__main__" :
    obj = server()
    threading.Thread(target = obj.initialiser).start()

