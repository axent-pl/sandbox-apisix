FROM golang:1.21.4

WORKDIR /app
COPY go.mod main.go ./
RUN go mod download

RUN CGO_ENABLED=0 GOOS=linux go build -o /docker-server

EXPOSE 8080

CMD ["/docker-server"]