FROM golang:1.20.2 AS builder 

WORKDIR /app

COPY go.mod go.sum /app/

RUN go mod download

COPY . .

RUN go build -o build/fizzbuzz

FROM gcr.io/distroless/base

COPY --from=builder /app/build/fizzbuzz /fizzbuzz

COPY --from=builder /app/templates /templates

CMD ["/fizzbuzz", "serve", "--port=8080"]
