#!/bin/bash

python3 tools/generate-routes.py 100 apisix-standalone 1> services/apisix-gateway-standalone/conf/apisix.yaml
python3 tools/generate-routes.py 1000 apisix-decoupled 1> services/apisix-gateway-decoupled/routes.yaml
python3 tools/generate-routes.py 100 kong-standalone 1> services/kong-gateway/kong.yaml
python3 tools/generate-routes.py 1000 kong-decoupled 1> services/kong-gateway/kong-decoupled.yaml