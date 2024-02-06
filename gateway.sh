#!/bin/bash


echo "$@"

if [ "$@" == "down" ]; then
    echo "Stopping API Gateway..."
    docker-compose down gateway-dashboard
    docker-compose down gateway
    docker-compose down gateway-db
elif [ "$@" == "up" ]; then
    echo "Starting API Gateway..."
    docker-compose up -d --build gateway-db
    sleep 10
    docker-compose up -d --build gateway
    docker-compose up -d --build gateway-dashboard
fi