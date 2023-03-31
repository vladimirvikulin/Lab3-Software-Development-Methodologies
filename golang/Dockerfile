FROM golang:1.20.2

WORKDIR /app

COPY go.mod go.sum /app/

RUN go mod download

COPY . .

RUN go build -o build/fizzbuzz

CMD ["./build/fizzbuzz", "serve", "--port=8080"]
