# TCP Chat server

Sockets are an interfeace which work based on TCP/IP principles to send and recieve data. Just like any other TCP/IP protocol based interaction, the two way communication between two sockets is set up by SYN, SYN-ACK and ACK.

The TCP sockets require only :

1.IP Adress
2.Port

to communicate hence making it very versatile.

In our case, we use Stream sockets, which are connection oriented sockets and follow the TCP protocol wherein the data is sequenced and in order, unlike the UDP protocol.

Both scripts are implemented in python.

The server.py runs a TCP chat server which opens a socket of its own and binds it to its own address. This open socket listens and accepts TCP connections from other client sockets and decides wether to accept them or not.The server also runs threads to be able to accept multiple clients and allow interaction between them.There is also a functionality to kick a user by providing the IP and port of the client socket using /leave (/leave <User IP> <User port>)

The client.py runs a client script which opens a socket and connects to the socket of the server. There are text formatting options in the messages such as:
	/colour tag which can change the colour of the 	text (/colour <colour> "texthere")
	**text** for bold text
	__text__ for italics text
	~~text~~ for strikethrough text


	
