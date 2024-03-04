FROM golang:1.21.4

# httpster
WORKDIR /app
COPY code/ /app/
RUN go mod download && \
    make build && \
    mkdir -p /app/results

# apache benchmark & wrk
RUN apt update && \
    apt install -y wrk apache2-utils python3-requests

# RUN pip3 install requests

COPY scripts/ /app/
COPY docker-entrypoint.sh /docker-entrypoint.sh

VOLUME [ "/app/results" ]
ENTRYPOINT [ "/docker-entrypoint.sh" ]