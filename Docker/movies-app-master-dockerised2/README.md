Dockerisation of a MERN stack movie application!


Prerequisites:
Have both Docker and Docker Compose on your system

To build the contents of the repo:

1.Download/clone the repository
2.On a command line interface enter the following command:
	"docker compose up"

This command will build the necessary images which contain our application and then create the different containers based on those images!
Note: If there are privilege issues then use sudo

To test out the movie application, we can go to port 3000 on localhost using a web browser and if all went well, the application should be running! 


Behind the scenes?

How was this MERN application containerised used Docker?
One could simply run the docker command with its various tags and run the apllications in an interconnected manner. But it is far far simpler to do it using docker compose.

A docker file was added to both the client side and server side of the application. This file contains instructions for docker on the specifications(such as working directory,networks,ports and volumes) while creating the container. 	

To create and run both the containers in an interconnected manner, we create a Docker compose file which contains details about services and their specifications.
The docker compose module will run all these services(aka containers) together and create a interconnected multi container ready to use application that is portable.
In our current example, the three containers formed are: frontclient,server, mongodb. 




