FROM apache/apisix-dashboard:3.0.1-alpine
COPY --chown=apisix:apisix conf.yaml /usr/local/apisix-dashboard/conf/conf.yaml
COPY --chown=apisix:apisix schema.json /usr/local/apisix-dashboard/conf/schema.json
COPY --chown=apisix:apisix docker-entrypoint.sh /docker-entrypoint.sh

ENTRYPOINT [ "/docker-entrypoint.sh" ]