#!/usr/bin/env sh

set -eo pipefail

echo "$(sed 's/${DB_A6DC_HOST}/'$DB_A6DC_HOST'/g' /usr/local/apisix-dashboard/conf/conf.yaml)" > /usr/local/apisix-dashboard/conf/conf.yaml
echo "$(sed 's/${DB_A6DC_PORT}/'$DB_A6DC_PORT'/g' /usr/local/apisix-dashboard/conf/conf.yaml)" > /usr/local/apisix-dashboard/conf/conf.yaml

/usr/local/apisix-dashboard/manager-api