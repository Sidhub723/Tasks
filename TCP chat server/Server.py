###############################Server ##########################

global coldict 
#colour data as well as bold, italics etc!

coldict = {
'CEND'      : '\33[0m',
'CBOLD'     : '\33[1m',
'CITALIC'   : '\33[3m',
'CURL'      : '\33[4m',
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

import socket
import sys
import time
import threading
import pprint

serverip = "" # some server ip address
serverport = 5555
count = 0

class server():
    def __init__(self):
        self.clients = []

    
    def initialiser(self):
        try:
            serversock = socket.socket()
            serversock.bind((serverip,serverport))   # BINDING the socket to the ip of the server itself and a port on it so that all incoming connection recieved by the socket are redirected to the server itself
            serversock.listen(30)  # the socket is now listening on a port on the ip of the server

            while True:
                clisock,addr = serversock.accept()  # accepting any socket connections while the server socket is listening
                a = input("A connection has arrived from "+ addr[0]+ " via port "+addr[1] +" \n Do you want to accept it?? Y/N")
                if a == 'N' | a == 'n' :
                    clisock.close()

                elif a =='y' | a == 'Y' :

                    count += 1
                    print("Client has joined. IP : "+addr[0] + " , and via port : "+addr[1]+ " at time : "+time.strftime("%a, %d %b %Y %H:%M:%S" + " . \n")) # visible to the person running server
                    print(count + " clients currently online")
                    self.broadcaster(str("User has joined room! Total online users are "+count))  # message broadcasted to all other active users
                    self.clients.append(clisock)
                    threading.Thread(target = self.clienthandler(),args = (clisock,)).start()
                    
                else :
                    print("Wrong input :(")

                #inp = input("Enter commands if any. If nothing then just enter 'N' ")
                #if inp == "/leave":
                #    iprem = input("Enter the IP adress and port to be removed as a tuple")
                    

                



            #serversock.close()
        except socket.error as txt:
            print("Could not start server thread :(")
            time.sleep(4)
            sys.exit()




    def broadcaster(self,message):
        for c in self.clients:
            try:
                c.send(message.encode("utf-8"))

            except socket.error as txt :
                c.send(b'The message failed to send :( \n Try to send it again or close and reopen your connection! ')

        


    def clienthandler(self,ClientsSocket):
        global col
        ClientsSocket.send(b'Welcome to the chat server! You should now be able to view messages from others, as well as post your own \n If you want to leave the chatroom then type /leave \n Enjoy your stay!')

        while True :
            data = ClientsSocket.recv(1024)
            #if not data :
            #    break
            if str(data) == '/leave':   # /leave is the keyword for the client to close his connection
                break 
            
            #formatting the data here as per the task!
            coltype = ''
            if "/colour" in str(data):      #changing colour
                ind = str(data).index('/')
                ind = ind + 8 # index of thr first letter of the actual colour
                end = str(data).index(' ',ind)
                colo = str(data)[ind,end].upper()
                for keys in coldict.keys :
                    if colo in keys:
                        coltype = coldict[keys]
                data = coldict[coltype] + str(data) + coldict('CEND')

            if "/leave" in str(data):
                self.broadcaster("A user has left")
                self.clients.remove(ClientsSocket)
                count -= 1
                ClientsSocket.close()

            if "/private" in str(data):
                pass
                #open a new socket between requester and requested client?
                
            if str(data).count("**") == 2 : #wont work if there are multiple such bold text aesterisks 
                start = str(data).index("**")
                end = str(data).index("**",start+1)
                data = coldict['CBOLD'] + str(data) + coldict('CEND')







            for client in self.clients.values():
                client.send(data)

        self.clients.remove(ClientsSocket) # removes from list of active clients
        count -= 1
        ClientsSocket.close() # also closes the clients connection


if __name__ == "__main__" :
    obj = server()
    threading.Thread(target = obj.initialiser).start()


