FROM golang:1.21.4

WORKDIR /app
COPY code/ /app/
RUN go mod download
RUN make build

ENTRYPOINT [ "/app/bin/httpster" ]