FROM node:18.15.0 as builder

WORKDIR /app

COPY package.json package-lock.json /app/

RUN npm ci 

ENV NODE_ENV=production

COPY index.js /app/

FROM astefanutti/scratch-node

COPY --from=builder /app /

ENTRYPOINT  ["node", "index.js", "--port=8080"]