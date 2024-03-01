FROM golang:1.21.4

# httpster
WORKDIR /app
COPY code/ /app/
RUN go mod download && \
    make build

# apache benchmark & wrk
RUN apt update && \
    apt install -y wrk apache2-utils

ENTRYPOINT [ "/app/bin/httpster" ]