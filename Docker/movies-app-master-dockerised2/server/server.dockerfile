FROM node:18-slim
WORKDIR /usr/src/app
COPY ./package.json ./
COPY ./yarn.lock ./
RUN yarn install
RUN npm install
#RUN npm ci
COPY . .
EXPOSE 3000
CMD ["yarn","start"]






# Node image is a plain old image from docker hub
# Ne install our application with its dependencies(express) based on what is specified in package.json
# Our custom image which is a combiantion of the base nodejs image and also our additional source code
# When we run the container and check the container will run the node applicaion in the /app directory . all copied files also will land there
# Then we copy the package.json which contains info about all our dependencies into the working directory /app
# Then we actually have to install our dependencies in our docker container so we run a npm install to install express and yarn install to install yarn
# . indicates the current working directory
# The name of the container is the same name as that of the service (by default). A different name can be specified using container_name argument 
# Then we copy everything from the current directory of our system onto the working directory on the docker container
# We copy the package.json first because -- optimisation by caching. it images form layer by layer and the result is cached at every single layer
# The index.js file tells us that the nodejs application is listening on port 3000 so we'll indicate that port 3000 is to be used
# Then when it creates the container, it runs the index.js(the actual starting file for the application) file to actually run the application
# We can now build our docker container by running the command "docker build ." or "docker build <whatever is the filepath containing the application>" 
# While building we can pass the -t flag to the command and give it a name
# We can view our image by running "docker image ls"
# If we didnt want to copy any files we could add them in a .dockerignore file



