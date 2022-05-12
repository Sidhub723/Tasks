FROM node:18-slim
WORKDIR /usr/src/app
COPY ./package.json /usr/src/app/
COPY ./yarn.lock /usr/src/app/
RUN yarn install
RUN npm install
COPY . /usr/src/app/
#ENV     
EXPOSE 3000
CMD ["yarn","start"]
