FROM node:18.15.0

WORKDIR /app

COPY package.json package-lock.json /app/

RUN npm ci

ENV NODE_ENV=production

COPY index.js /app/

CMD ["node", "index.js", "--port=8080"]