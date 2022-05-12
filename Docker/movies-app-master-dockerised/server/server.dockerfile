FROM node:18-slim
WORKDIR /usr/src/app
COPY ./package.json /usr/src/app/
COPY ./yarn.lock /usr/src/app/
RUN yarn install
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node","index.js"]






# node image is a plain old image from docker hub
# we install our application with its dependencies(express) here and create our custom image which is a combiantion of the base nodejs image and also our additional source code
# when we run the container and check the container will run the node applicaion in the /app directory . all copied files also will land there
# then we copy the package.json which contains info about all our dependencies into the working directory /app
# then we actually have to install our dependencies in our docker container so we run a npm install to install express and yarn install to install yarn
# . and ./ are the same thing and they indicate the current working directory
# then we copy everything from the current directory of our system onto the docker file
# we copy the package.json first because -- optimisation by caching. it images form layer by layer and the result is cached at every single layer
# the index.js file tells us that the nodejs application is listening on port 3000 so we'll open port 3000 for the application on it
# then when it creates the container, it runs the index.js(the actual starting file for the application) file to actually run the application
# we can now build our docker container by running the command "docker build ." or "docker build <whatever is the filepath containing the application>" 
# while building we can pass the -t flag to the command and give it a name
# also, to allow external access to the docker container, we also add the -p flag as -p <external port/our port>:<docker port> . In this case container port will be 3000, the localhost port can be any open port
# we can view our image by running "docker image ls"
# if we didnt want to copy any files we could add them in a .dockerignore file



