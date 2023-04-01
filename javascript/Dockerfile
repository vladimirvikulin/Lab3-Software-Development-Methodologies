FROM node:latest as builder

WORKDIR /app

COPY package.json package-lock.json /app/

RUN npm ci 

ENV NODE_ENV=production

COPY index.js /app/

FROM gcr.io/distroless/nodejs

COPY --from=builder /app /

CMD ["index.js", "--port=8080"]