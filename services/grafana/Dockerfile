FROM grafana/grafana:7.3.7

COPY --chown=grafana:root provisioning/datasources/loki-datasource.yaml /etc/grafana/provisioning/datasources/
COPY --chown=grafana:root provisioning/datasources/prometheus-datasource.yaml /etc/grafana/provisioning/datasources/
COPY --chown=grafana:root provisioning/dashboards/all.yaml /etc/grafana/provisioning/dashboards/
COPY --chown=grafana:root dashboards/apisix-dashboard.json /var/lib/grafana/dashboards/
COPY --chown=root:root grafana.ini /etc/grafana/grafana.ini