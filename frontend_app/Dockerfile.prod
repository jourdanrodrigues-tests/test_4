FROM node:9.11.1

WORKDIR /app/

ARG API_URL

COPY package.json package-lock.json ./

RUN npm i

COPY . .

RUN npm run build
