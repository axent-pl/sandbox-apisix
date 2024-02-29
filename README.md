# sandbox-apisix
APISIX API Gateway sandbox

## Usage

Start one or more available profiles

```shell
# start APISIX standalone
docker-compose --profile apisix-standalone

# start APISIX decoupled
docker-compose --profile apisix-decoupled

# start Kong standalone
docker-compose --profile kong-standalone

# start Kong decoupled
docker-compose --profile kong-decoupled
```

## Links

- [Keycloak](http://localhost:2380/auth/)

- [Grafana](http://localhost:3000)

- [APISIX standalone API](http://localhost:9081)

- [APISIX decoupled API](http://localhost:9080)

- [APISIX decoupled GUI](http://localhost:9000)